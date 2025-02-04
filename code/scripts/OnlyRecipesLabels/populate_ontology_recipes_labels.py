import argparse
import copy

from rdflib import Graph, Literal, Namespace, OWL, RDF, RDFS, URIRef
import pickle as pkl
from tqdm import tqdm


def populates_recipes(onto, dataset, fsrecipe_ns, path_to_info_recipes, path_to_updated_onto):

    recipes_info_json = pkl.load(open(path_to_info_recipes, "rb"))
    recipes_names_id = recipes_info_json["recipes_names_id"]
    recipes_names_list = list(recipes_names_id.keys())
    recipes_names_list.sort()


    # recipe class
    recipe_dataset_class = fsrecipe_ns[dataset]

    for recipe_name in tqdm(recipes_names_list):
        recipe_name_no_index = recipe_name.split("#")[0]
        #print(recipes_names_id[recipe_name])
        #if recipes_names_id[recipe_name] == "Recipe1m-4664": breakpoint()
        # Create instance URI
        recipe_instance = fsrecipe_ns["Recipe-{}".format(recipes_names_id[recipe_name])]

        # Add the instance as a member of the recipe_dataset class
        onto.add((recipe_instance, RDF.type, recipe_dataset_class))
        # Add the label to the instance
        onto.add((recipe_instance, RDFS.label, Literal(recipe_name_no_index)))

    # Serialize the updated onto to a file
    onto.serialize(path_to_updated_onto, format="ttl")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate ontologies")
    parser.add_argument("-path_to_info_recipes_recipe1m", type=str, default="../InfoRecipes/PklFiles/Recipe1m_recipes_info.pkl")
    parser.add_argument("-path_to_info_recipes_tasty",  type=str, default="../InfoRecipes/PklFiles/Tasty_recipes_info.pkl")
    parser.add_argument("-path_to_save", type=str, default="../Ontologies/")
    parser.add_argument("-populate", type=str, default="all", help="all = (recipe1m + tasty), recipe1m, tasty")

    args = parser.parse_args()

    path_to_info_recipes_recipe1m = args.path_to_info_recipes_recipe1m
    path_to_info_recipes_tasty = args.path_to_info_recipes_tasty
    path_to_save = args.path_to_save
    populate = args.populate

    # Create an RDF Graph for the ontology
    onto_recipesl = Graph()
    base_URI = URIRef("https://w3id.org/fuskg/temporal-recipes-steps")
    onto_recipesl .bind("", base_URI)
    # Add a statement to the (new) ontology indicating the import of the existing ontology (fuskg-recipes)
    onto_recipesl.bind("owl", OWL)
    # "https://horus-ai.fbk.eu/fuskg/ontology/fuskg-recipes.ttl"
    onto_recipesl.add(
        (base_URI, OWL.imports, URIRef("https://raw.githubusercontent.com/IDA-FBK/FuS-KG/refs/heads/update-modules/ontology/TBox/fuskg-recipes.ttl")))


    fsrecipe_ns = Namespace("https://w3id.org/fuskg/recipe#")
    onto_recipesl.bind("fsreci", fsrecipe_ns)

    if populate == "all":
        onto_tmp = copy.deepcopy(onto_recipesl)
        path_to_updated_onto = path_to_save + "fuskg-recipes-labels-recipe1m.ttl"
        populates_recipes(onto_recipesl, "Recipe1m", fsrecipe_ns, path_to_info_recipes_recipe1m, path_to_updated_onto)
        path_to_updated_onto = path_to_save + "fuskg-recipes-labels-tasty.ttl"
        populates_recipes(onto_tmp, "Tasty", fsrecipe_ns, path_to_info_recipes_tasty, path_to_updated_onto)
    elif populate == "recipe1m":
        path_to_updated_onto = path_to_save + "fuskg-recipes-labels-recipe1m.ttl"
        populates_recipes(onto_recipesl, "Recipe1m", fsrecipe_ns, path_to_info_recipes_recipe1m, path_to_updated_onto)
    elif populate == "tasty":
        path_to_updated_onto = path_to_save + "fuskg-recipes-labels-tasty.ttl"
        populates_recipes(onto_recipesl, "Tasty",  fsrecipe_ns, path_to_info_recipes_tasty, path_to_updated_onto)
