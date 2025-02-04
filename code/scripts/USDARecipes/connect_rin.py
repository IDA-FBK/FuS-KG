import argparse
import os.path

from rdflib import Graph, Namespace, OWL, RDF, URIRef, XSD, Literal
import pandas as pd
import pickle as pkl


def create_connection_recipefood(onto_recipe, usda_ns, fsreci_ns, fsfood_ns, recipes_info, map_food_usda, recipe_food_weights, path_to_updated_onto):
    recipes_titles = recipe_food_weights["Recipe Title"].tolist()
    recipes_foods = recipe_food_weights["Ingredient"].tolist()
    recipes_foods_weights = recipe_food_weights["Weight"].tolist()
    recipes_names_id = recipes_info["recipes_names_id"]

    rf_instances_created = []

    missing_ingredients_for_recipe = {"Recipes":[], "Ingredients":[]}

    for r_title, r_food, rfweight in zip(recipes_titles, recipes_foods, recipes_foods_weights):
        print("Processing recipe:  {}".format(r_title))
        r_id = recipes_names_id[r_title]
        r_instance = fsreci_ns["Recipe-{}".format(r_id)]
        r_food_lower = r_food.lower()

        if r_food_lower not in map_food_usda:
            missing_ingredients_for_recipe["Recipes"].append(r_title)
            missing_ingredients_for_recipe["Ingredients"].append(r_food_lower)
        else:
            food_id = map_food_usda[r_food_lower]
            amount_of_food = round(rfweight, 2)

            # recipe food instance
            rf_instance = fsreci_ns["RECIPEFOOD-{}-{}".format(food_id, amount_of_food)]

            if rf_instance not in rf_instances_created:
                rf_instances_created.append(rf_instance)
                # Add the instance as a member of the RecipeFood class
                onto_recipe.add((rf_instance, RDF.type, fsreci_ns["RecipeFood"]))

                # Add the object property hasFood to recipe food
                onto_recipe.add((rf_instance, fsreci_ns.hasFood, usda_ns[food_id]))

                # Add the data property amountOfFood to recipe food
                onto_recipe.add((rf_instance, fsreci_ns.amountFood, Literal(amount_of_food, datatype=XSD.double)))

            # Add the object property recipe food to the recipe instance
            onto_recipe.add((r_instance, fsreci_ns.hasRecipeFood, rf_instance))



    onto_recipe.serialize(path_to_updated_onto, format="ttl")
    missing_ingredients_for_recipe = pd.DataFrame(missing_ingredients_for_recipe, index=None)
    missing_ingredients_for_recipe.to_csv("missing_ingredients_for_recipe.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate ontologies")
    parser.add_argument("-path_to_recipe_ontology", type=str, default="../Ontologies/fuskg-recipes-labels-recipe1m.ttl")
    #parser.add_argument("-path_to_recipe_tasty_ontology", type=str, default="./ontologies/updated_ontology_recipe_tasty.ttl")
    parser.add_argument("-path_to_map_food_usda", type=str, default="./useful_files/map_food_usda.pickle")
    parser.add_argument("-path_to_recipes_info", type=str, default="../InfoRecipes/PklFiles/Recipe1m_recipes_info.pkl")
    parser.add_argument("-path_to_ingrsw", type=str, default="../InfoRecipes/Ingredients/recipe_ingredients_recipe1m_edited.csv")

    parser.add_argument("-path_to_save", type=str, default="../Ontologies/")
    parser.add_argument("-dataset", type=str, default="Recipe1m")

    args = parser.parse_args()

    path_to_recipe_ontology = args.path_to_recipe_ontology
    path_to_ingrsw = args.path_to_ingrsw
    path_to_recipes_info = args.path_to_recipes_info
    path_to_map_food_usda = args.path_to_map_food_usda
    path_to_save = args.path_to_save
    dataset = args.dataset

    print("\n ---- Processing {} ---- \n".format(dataset))
    print("  PATH TO RECIPE ONTOLOGY {}".format(path_to_recipe_ontology))
    print("  PATH TO RECIPE INFO = {}".format(path_to_recipes_info))
    print("  PATH TO MAP FOOD USDA = {}".format(path_to_map_food_usda))

    recipes_info = pkl.load(open(path_to_recipes_info, "rb"))
    recipe_food_weights = pd.read_csv(path_to_ingrsw)
    map_food_usda = pkl.load(open(path_to_map_food_usda, "rb"))

    # Create an RDF Graph
    onto_recipe = Graph()

    # Load the recipe ontology from a local file
    onto_recipe.parse(path_to_recipe_ontology, format="ttl")

    base_URI = URIRef("https://w3id.org/fuskg/recipes-recipe1m-usda")
    onto_recipe.bind("", base_URI)

    onto_recipe.bind("owl", OWL)
    # https://horus-ai.fbk.eu/fuskg/ontology/fuskg-usda.ttl
    onto_recipe.add(
        (base_URI, OWL.imports, URIRef("https://media.githubusercontent.com/media/IDA-FBK/FuS-KG/refs/heads/update-modules/ontology/ABox/fuskg-usda-foods-nutrients.ttl")))
    onto_recipe.add(
        (base_URI, OWL.imports, URIRef(
            "https://media.githubusercontent.com/media/IDA-FBK/FuS-KG/refs/heads/update-modules/ontology/TBox/fuskg-recipes.ttl")))

    # Define the namespace for the ontology
    usda_ns = Namespace("https://w3id.org/fuskg/usda#")
    fsreci_ns = Namespace("https://w3id.org/fuskg/recipe#")
    fsfood_ns = Namespace("https://w3id.org/fuskg/food#")

    onto_recipe.bind("usda", usda_ns)
    onto_recipe.bind("fsreci", fsreci_ns)
    onto_recipe.bind("fsfood", fsfood_ns)
    path_to_updated_onto = path_to_save + "USDA-Recipes_{}_complete2.ttl".format(dataset)
    create_connection_recipefood(onto_recipe, usda_ns, fsreci_ns, fsfood_ns, recipes_info, map_food_usda, recipe_food_weights, path_to_updated_onto)
