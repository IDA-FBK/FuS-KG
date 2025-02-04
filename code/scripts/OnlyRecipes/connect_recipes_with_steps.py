import argparse

from rdflib import Graph, Namespace
import pickle as pkl
from tqdm import tqdm


def create_connection(onto_recipes_labels, onto_steps, fsreci_ns, fstemp_ns, recipes_info, path_to_updated_onto):

    merged_onto = onto_recipes_labels + onto_steps

    recipes_names_id = recipes_info["recipes_names_id"]
    recipes_names_list = list(recipes_names_id.keys())
    recipes_names_list.sort()
    recipes_steps = recipes_info["recipes-steps"]

    for recipe_name in tqdm(recipes_names_list):
        recipe_id = recipes_names_id[recipe_name]
        recipe_instance = fsreci_ns["Recipe-{}".format(recipe_id)]
        # if there are steps for the current recipe
        if recipes_steps[recipe_id]:
            recipe_first_step = recipes_steps[recipe_id][0]

            # Add the object property hasFirstRecipeStep to recipe
            merged_onto.add((recipe_instance, fstemp_ns.hasFirstRecipeStep, recipe_first_step))

    merged_onto.serialize(path_to_updated_onto, format="ttl")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate ontologies")
    parser.add_argument("-path_to_recipe_labels_ontology", type=str, default="../Ontologies/fuskg-recipes-labels-recipe1m.ttl")
    parser.add_argument("-path_to_recipesteps_ontology", type=str, default="../Ontologies/fuskg-temporal-recipe-steps-recipe1m_tmp.ttl")
    parser.add_argument("-path_to_info_recipes", type=str, default="../InfoRecipes/PklFiles/Recipe1m_recipes_info.pkl")
    parser.add_argument("-path_to_save", type=str, default="../Ontologies/")
    parser.add_argument("-dataset", type=str, default="recipe1m")

    args = parser.parse_args()

    path_to_recipe_labels_ontology = args.path_to_recipe_labels_ontology
    path_to_recipesteps_ontology = args.path_to_recipesteps_ontology
    path_to_info_recipes = args.path_to_info_recipes
    path_to_save = args.path_to_save
    dataset = args.dataset

    print("\n ---- Processing {} ---- \n".format(dataset))
    print("  PATH TO RECIPE ONTOLOGY {}".format(path_to_recipe_labels_ontology))
    print("  PATH TO RECIPE STEPS ONTOLOGY {}".format(path_to_recipesteps_ontology))
    print("  PATH TO INFO RECIPES = {}".format(path_to_info_recipes))

    # Create an RDF Graph
    onto_recipe_labels = Graph()
    onto_rsteps = Graph()

    # Load the recipe ontology from a local file
    onto_recipe_labels.parse(path_to_recipe_labels_ontology, format="ttl")
    # Load the recipe steps ontology from a local file
    onto_rsteps.parse(path_to_recipesteps_ontology, format="ttl")
    recipes_info = pkl.load(open(path_to_info_recipes, "rb"))

    #recipe_steps_ns = Namespace("http://www.semanticweb.org/tania/ontologies/2023/9/recipe-steps-ont")
    fsreci_ns = Namespace("https://w3id.org/fuskg/recipe#")
    fstemp_ns = Namespace("https://w3id.org/fuskg/temporal#")
    path_to_updated_onto = path_to_save + "fuskg-recipes-recipessteps-{}_final.ttl".format(dataset)

    create_connection(onto_recipe_labels, onto_rsteps, fsreci_ns, fstemp_ns, recipes_info, path_to_updated_onto)
