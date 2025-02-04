import argparse
from collections import Counter
import copy
import math
import os

import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef, OWL
from rdflib.namespace import XSD
import pickle as pkl
from tqdm import tqdm


def populate_description_steps(onto, temp_ns, path_to_steps, path_to_updated_onto):
    recipe_steps = pd.read_csv(path_to_steps)["Step"].tolist()
    recipe_steps.sort()

    # create the updated ontology only if it does not exist
    if not os.path.exists(path_to_updated_onto):
        # Iterate over the list and create instances of RecipeStep with descriptions
        for index, description in enumerate(tqdm(recipe_steps)):
            # Create instance URIs with a progressive ID
            dstep_instance = temp_ns[f"DescriptionStep-{index+1}"]

            # Add the instance as a member of the StepDescription class
            onto.add((dstep_instance, RDF.type, temp_ns.StepDescription))

            # Add the data property stepDescription with the step's description
            onto.add((dstep_instance, temp_ns.stepDescription, Literal(description, datatype=XSD.string)))

        # Serialize the updated graph to a file
        onto.serialize(path_to_updated_onto, format="ttl")
        print("Creation: {} --- done".format(path_to_updated_onto))
    else:
        print("Already exists: {} --- skip".format(path_to_updated_onto))
    return recipe_steps


def find_duplicates(elements_list):
    counter = Counter(elements_list)
    duplicates = [item for item, count in counter.items() if count > 1]

    return duplicates


def populates_recipes_steps(onto, dataset, recipe_ns, recipes_steps, path_to_recipes, path_to_updated_onto):
    recipes_df = pd.read_csv(path_to_recipes)

    recipes_names = recipes_df["Recipe"].tolist()
    steps_recipes = [c for c in recipes_df.columns if "step" in c]
    max_steps = len(steps_recipes)

    # create the updated ontology only if it does not exist
    if not os.path.exists(path_to_updated_onto):

        # dictionary containing for each recipe-id the tracks of its steps
        recipes_steps_tracks = {}
        # dictionary containing for each recipe-name its corresponding recipe name
        recipes_name_id = {}

        for step in tqdm(range(1, max_steps+1)):
            current_step = "step-{}".format(step)
            if current_step in steps_recipes:
                current_step_descriptions = recipes_df[current_step].tolist()
                current_step_int = int(current_step.split("-")[-1])
                if dataset == "Tasty":
                    current_step_trange = recipes_df["trange-{}".format(step)].tolist()

                for i, csd in enumerate(tqdm(current_step_descriptions)):

                    if isinstance(csd, str) or not math.isnan(csd) or current_step_int == 1:

                        recipe_code = "{}-{}".format(dataset, i+1)

                        if recipe_code not in recipes_steps_tracks:
                            recipes_name_id[recipes_names[i]+"#{}".format(i+1)] = recipe_code
                            recipes_steps_tracks[recipe_code] = []

                        if isinstance(csd, str) or not math.isnan(csd):
                            csd_id = recipes_steps.index(csd)
                            #recipes_steps_tracks[recipe_code].append(csd_id)

                            # Create instance URIs with a progressive ID
                            rstep_instance = recipe_ns["RecipeStep-{}-{}".format(recipe_code, step)]
                            recipes_steps_tracks[recipe_code].append(rstep_instance)

                            # Add the instance as a member of the RecipeStep class
                            onto.add((rstep_instance, RDF.type, recipe_ns.RecipeStep))

                            # Add the object property hasStepDescription to the recipe step instance
                            onto.add((rstep_instance, recipe_ns.hasStepDescription, recipe_ns["DescriptionStep-{}".format(csd_id+1)]))

                            # Add the data properties ordered_step_begin and ordered_step_end to the recipe step instance
                            if dataset == "Tasty":
                                rstep_trange = [int(num) for num in current_step_trange[i].split(",")]
                                onto.add((rstep_instance, recipe_ns.orderedStepBegin, Literal(rstep_trange[0], datatype=XSD.float)))
                                onto.add((rstep_instance, recipe_ns.orderedStepEnd, Literal(rstep_trange[1], datatype=XSD.float)))

                            prev_step = step - 1

                            if prev_step >= 1:
                                # Add the object property beforeStep to the recipe step instance
                                onto.add((rstep_instance, recipe_ns.beforeStep, recipe_ns["RecipeStep-{}-{}-{}".format(dataset, i+1, prev_step)]))
                                # Add the object property afterStep to the previous instance instance
                                onto.add((recipe_ns["RecipeStep-{}-{}-{}".format(dataset, i+1, prev_step)], recipe_ns.afterStep, rstep_instance))

        # Serialize the updated graph to a file
        onto.serialize(path_to_updated_onto, format="ttl")
        duplicates_recipes = find_duplicates(recipes_names)
        with open("./{}_recipes_info.pkl".format(dataset), "wb") as tmpf:
            # this file contains for each recipe its corresponding uri steps, it also contains the duplicated recipes
            # (i.e., recipe with same names but different set of instructions)
            pkl.dump({"recipes_names_id": recipes_name_id, "recipes-steps": recipes_steps_tracks, "duplicates": duplicates_recipes}, tmpf)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate ontologies")
    parser.add_argument("-path_to_recipes_recipe1m", type=str, default="./Steps/Recipe_V1/RECIPE_1.3/recipe-steps-RECIPE1M-1.3-CLEANED.csv")
    parser.add_argument("-path_to_recipes_tasty",  type=str, default="./Steps/Recipe_V1/RECIPE_1.3/recipe-steps-TASTY-1.3-CLEANED.csv")
    parser.add_argument("-path_to_unique_steps",  type=str, default="./Steps/Recipe_V1/RECIPE_1.3/recipe-steps-UNIQUE_STEPS-1.3-CLEANED.csv")
    parser.add_argument("-path_to_save", type=str, default="../Ontologies/")
    parser.add_argument("-populate", type=str, default="all", help="all = (recipe1m + tasty), recipe1m, tasty")

    args = parser.parse_args()

    path_to_recipes_recipe1m = args.path_to_recipes_recipe1m
    path_to_recipes_tasty = args.path_to_recipes_tasty
    path_to_unique_steps = args.path_to_unique_steps
    path_to_save = args.path_to_save
    populate = args.populate

    # Create an RDF Graph for the ontology
    onto_dsteps = Graph()
    base_URI = URIRef("https://w3id.org/fuskg/temporal-recipes-steps")
    onto_dsteps.bind("", base_URI)
    # Add a statement to the (new) ontology indicating the import of the existing ontology (fuskg-temporal)
    onto_dsteps.bind("owl", OWL)
    # https://horus-ai.fbk.eu/fuskg/ontology/fuskg-temporal.ttl
    onto_dsteps.add(
        (base_URI, OWL.imports, URIRef("https://raw.githubusercontent.com/IDA-FBK/FuS-KG/refs/heads/update-modules/ontology/TBox/fuskg-temporal.ttl")))

    fstemp_ns = Namespace("https://w3id.org/fuskg/temporal#")
    onto_dsteps.bind("fstemp", fstemp_ns)

    path_to_updated_onto = path_to_save+"fuskg-temporal-description-steps.ttl"
    recipe_steps = populate_description_steps(onto_dsteps, fstemp_ns, path_to_unique_steps, path_to_updated_onto)


    if populate == "all":
        onto_tasty = copy.deepcopy(onto_dsteps)
        path_to_updated_onto = path_to_save + "fuskg-temporal-recipe-steps-recipe1m_tmp.ttl"
        populates_recipes_steps(onto_dsteps, "Recipe1m", fstemp_ns, recipe_steps, path_to_recipes_recipe1m, path_to_updated_onto)
        path_to_updated_onto = path_to_save + "fuskg-temporal-recipe-steps-tasty_tmp.ttl"
        populates_recipes_steps(onto_tasty, "Tasty", fstemp_ns, recipe_steps, path_to_recipes_tasty, path_to_updated_onto)
    elif populate == "recipe1m":
        path_to_updated_onto = path_to_save + "fuskg-temporal-recipe-steps-recipe1m_tmp.ttl"
        populates_recipes_steps(onto_dsteps, "Recipe1m", fstemp_ns, recipe_steps, path_to_recipes_recipe1m, path_to_updated_onto)
    elif populate == "tasty":
        path_to_updated_onto = path_to_save + "fuskg-temporal-recipe-steps-tasty_tmp.ttl"
        populates_recipes_steps(onto_dsteps, "Tasty", fstemp_ns, recipe_steps, path_to_recipes_tasty, path_to_updated_onto)
