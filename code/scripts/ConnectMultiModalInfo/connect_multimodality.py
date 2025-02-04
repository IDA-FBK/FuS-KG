import argparse

import json
from rdflib import Graph, Namespace, OWL, RDF, RDFS, URIRef, XSD, Literal
from rdflib.namespace import DCTERMS
import pickle as pkl

from tqdm import tqdm


def add_modalities_entities(onto_mm, fsmumo_ns, metadata, path_to_updated_onto, dataset):

    node_instances = {}
    if dataset == "Tasty":
        video_nodes = metadata.keys()
        for video_node in video_nodes:
            info = video_node.split("_")
            video_format = info[0]
            fps = info[1]
            w, h = info[2].split("x")
            # video node instance
            video_node_instance = fsmumo_ns["video-{}-{}-{}x{}".format(video_format, round(float(fps), 2), w, h)]

            # Add the instance as a member of the Video class
            onto_mm.add((video_node_instance, RDF.type, fsmumo_ns["Video"]))

            # Add the data properties fps, w, h to video node instance
            onto_mm.add((video_node_instance, fsmumo_ns.fps, Literal(fps, datatype=XSD.float)))
            onto_mm.add((video_node_instance, fsmumo_ns.width, Literal(w, datatype=XSD.int)))
            onto_mm.add((video_node_instance, fsmumo_ns.height, Literal(h, datatype=XSD.int)))

            # Add video format
            onto_mm.add((video_node_instance, DCTERMS.format, Literal("video/{}".format(video_format))))

            node_instances[video_node] = video_node_instance

    elif dataset == "Recipe1m":
        image_nodes = metadata.keys()

        for image_node in tqdm(image_nodes):
            info = image_node.split("_")
            img_format = info[0].lower()
            w, h = info[1].split("x")
            # image node instance
            image_node_instance = fsmumo_ns["image-{}-{}x{}".format(img_format, w, h)]

            # Add the instance as a member of the Video class
            onto_mm.add((image_node_instance, RDF.type, fsmumo_ns["Image"]))

            # Add the data properties fps, w, h to video node instance
            onto_mm.add((image_node_instance, fsmumo_ns.width, Literal(w, datatype=XSD.int)))
            onto_mm.add((image_node_instance, fsmumo_ns.height, Literal(h, datatype=XSD.int)))

            # Add image format
            onto_mm.add((image_node_instance, DCTERMS.format, Literal("image/{}".format(img_format))))

            node_instances["{}_{}x{}".format(img_format, w, h)] = image_node_instance


    onto_mm.serialize(path_to_updated_onto, format="ttl")
    return node_instances


def connect_mdr(onto_mm, fsreci_ns, fsmumo_ns, modality_node_instances, recipes_info, metadata, path_to_updated_onto, dataset):

    recipes_names_id = recipes_info["recipes_names_id"]

    md_instances_created_per_recipe = {}

    # recipe class
    recipe_dataset_class = fsreci_ns[dataset]
    if dataset == "Tasty":
        for i, (recipe_name, mm_info) in enumerate(metadata.items()):
            fps = round(mm_info["fps"], 2)

            recipe_name_no_index = recipe_name.split("#")[0]
            # get recipe istance
            recipe_code = recipes_names_id[recipe_name+"#{}".format(i+1)]
            r_instance = fsreci_ns["Recipe-{}".format(recipe_code)]
            # get mm instance
            mm_instance = modality_node_instances[mm_info["format"]+"_"+str(mm_info["fps"])+"_"+mm_info["resolution"]]

            name_md_recipe = "{}-video_{}".format(recipe_code, mm_info["format"]+"_"+str(fps)+"_"+mm_info["resolution"])

            if name_md_recipe not in md_instances_created_per_recipe:
                md_instances_created_per_recipe[name_md_recipe] = 1
            else:
                md_instances_created_per_recipe[name_md_recipe] += 1

            # create modal descriptor (md)
            md_instance = fsmumo_ns["{}-video_{}-{}".format(recipe_code, mm_info["format"]+"_"+str(fps)+"_"+mm_info["resolution"], md_instances_created_per_recipe[name_md_recipe])]

            # Add the instance as a member of the recipe_dataset class
            onto_mm.add((r_instance, RDF.type, recipe_dataset_class))

            # Add the label to the instance
            onto_mm.add((r_instance, RDFS.label, Literal(recipe_name_no_index)))

            # add hasPathInaArtifact data property to the current md
            onto_mm.add(
                (md_instance, fsmumo_ns.hasPathInArtifact, Literal("/Tasty_Videos_Dataset/ALL_RECIPES_without_videos/{}/recipe_video.mp4".format(recipe_name), datatype=XSD.string)))
            # add resourceURL data property to the current md
            onto_mm.add((md_instance, fsmumo_ns.resourceURL, Literal("https://fbk.sharepoint.com/:f:/s/IDA/EoA_tdSP9MpCo_ebxoOY7bwBztKr9asvB_pqNIjJ48p32w?e=f1qg6M", datatype=XSD.anyURI)))

            # Add the md instance as a member of the ModalDescriptor class
            onto_mm.add((md_instance, RDF.type, fsmumo_ns.ModalDescriptor))

            # connect recipe to md
            onto_mm.add((r_instance, fsmumo_ns.hasModalDescriptor, md_instance))

            # connect md to mm_instance
            onto_mm.add((md_instance, fsmumo_ns.hasModality, mm_instance))
    elif dataset == "Recipe1m":
        for id_recipe, recipe_info in metadata.items():
            recipe_name = recipe_info["title"]
            recipe_name_no_index = recipe_name.split("#")[0]
            recipe_images = recipe_info["images"]

            # get recipe istance
            #recipe_code = recipes_names_id[recipe_name]
            r_instance = fsreci_ns["Recipe-{}".format(id_recipe)]

            for recipe_image in tqdm(recipe_images):
                recipe_image_metadata = recipe_image["metadata"]
                img_format = recipe_image_metadata["format"].lower()
                img_width, img_height = recipe_image_metadata["width"], recipe_image_metadata["height"]
                img_path = recipe_image["url"]
                # get mm instance
                mm_instance = modality_node_instances["{}_{}x{}".format(img_format, img_width, img_height)]

                name_md_recipe = "{}-image_{}".format(id_recipe, img_format + "_{}x{}".format(img_width, img_height))
                if name_md_recipe not in md_instances_created_per_recipe:
                    md_instances_created_per_recipe[name_md_recipe] = 1
                else:
                    md_instances_created_per_recipe[name_md_recipe] += 1

                # create modal descriptor (md)
                md_instance = fsmumo_ns["{}-image_{}-{}".format(id_recipe, img_format + "_{}x{}".format(img_width, img_height),
                                                            md_instances_created_per_recipe[name_md_recipe])]

                # Add the instance as a member of the recipe_dataset class
                onto_mm.add((r_instance, RDF.type, recipe_dataset_class))

                # Add the label to the instance
                onto_mm.add((r_instance, RDFS.label, Literal(recipe_name_no_index)))

                # Add the md instance as a member of the ModalDescriptor class
                onto_mm.add((md_instance, RDF.type, fsmumo_ns.ModalDescriptor))

                # add resourceURL data property to the current md
                # onto_mm.add((md_instance, fsmumo_ns.resourceURL, Literal(img_url, datatype=XSD.anyURI)))
                # add hasPathInaArtifact data property to the current md
                onto_mm.add((md_instance, fsmumo_ns.hasPathInArtifact, Literal(img_path, datatype=XSD.string)))

                # add resourceURL data property to the current md
                onto_mm.add((md_instance, fsmumo_ns.resourceURL, Literal("https://fbk.sharepoint.com/:f:/s/IDA/EvsBg8UfMy5Cqh6lbrBAVn4BCWfBJq7Jks_6sRDD_kArAQ?e=oamRuY", datatype=XSD.anyURI)))

                # connect recipe to md
                onto_mm.add((r_instance, fsmumo_ns.hasModalDescriptor, md_instance))

                # connect md to mm_instance
                onto_mm.add((md_instance, fsmumo_ns.hasModality, mm_instance))


    onto_mm.serialize(path_to_updated_onto, format="ttl")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Populate ontologies")
    # parser.add_argument("-path_to_metadata", type=str, default="./Metadata/Tasty/metadata.json")
    # parser.add_argument("-path_to_grouped_metadata", type=str, default="./Metadata/Tasty/grouped_metadata.json")
    # parser.add_argument("-path_to_recipe_multimodal_base_ontology", type=str, default="./ontologies/recipe_multimodal_base.ttl")
    # parser.add_argument("-path_to_recipes_ontology", type=str, default="./ontologies/updated_ontology_recipe_tasty.ttl")
    # parser.add_argument("-path_to_recipes_info", type=str, default="./Tasty_recipes_info.pkl")
    #  python .\connect_multimodality.py -path_to_metadata .\Metadata\Tasty\metadata.json -path_to_grouped_metadata .\Metadata\Tasty\grouped_metadata.json -path_to_recipes_info ../InfoRecipes/PklFiles/Tasty_recipes_info.pkl -dataset Tasty

    parser.add_argument("-path_to_metadata", type=str, default="./Metadata/Recipe1m/merged_metadata.json")
    parser.add_argument("-path_to_grouped_metadata", type=str, default="./Metadata/Recipe1m/merged_grouped_metadata.json")
    parser.add_argument("-path_to_recipes_info", type=str, default="../InfoRecipes/PklFiles/Recipe1m_recipes_info.pkl")
    #
    parser.add_argument("-path_to_save", type=str, default="../Ontologies/")
    parser.add_argument("-dataset", type=str, default="Recipe1m")

    args = parser.parse_args()

    path_to_metadata = args.path_to_metadata
    path_to_grouped_metadata = args.path_to_grouped_metadata
    path_to_recipes_info = args.path_to_recipes_info

    path_to_save = args.path_to_save
    dataset = args.dataset

    print("\n ---- Processing {} ---- \n".format(dataset))
    print("  PATH TO METADATA {}".format(path_to_metadata))
    print("  PATH TO GROUPED METADATA {}".format(path_to_grouped_metadata))
    print("  PATH TO RECIPES INFO = {}".format(path_to_recipes_info))

    with open(path_to_metadata, 'r', encoding='utf-8') as jsonfile:
        metadata = json.load(jsonfile)

    with open(path_to_grouped_metadata, 'r', encoding='utf-8') as jsonfile:
        grouped_metadata = json.load(jsonfile)

    recipes_info = pkl.load(open(path_to_recipes_info, "rb"))

    onto_mm = Graph()
    base_URI = URIRef("https://w3id.org/fuskg/multimodal-recipes")
    onto_mm.bind("", base_URI)

    # Add a statement to the (new) ontology indicating the import of the existing ontology (fuskg-multimodal)
    onto_mm.bind("owl", OWL)
    onto_mm.add(
        (base_URI, OWL.imports, URIRef("https://raw.githubusercontent.com/IDA-FBK/FuS-KG/refs/heads/update-modules/ontology/TBox/fuskg-multimodal.ttl")))

    fsreci_ns = Namespace("https://w3id.org/fuskg/recipe#")
    fsmumo_ns = Namespace("https://w3id.org/fuskg/multimodal#")

    onto_mm.bind("fsreci", fsreci_ns)
    onto_mm.bind("fsmumo", fsmumo_ns)

    path_to_updated_onto = path_to_save + "fuskg-multimodal-{}_tmp.ttl".format(dataset)
    modality_node_instances = add_modalities_entities(onto_mm, fsmumo_ns, grouped_metadata, path_to_updated_onto, dataset)
    path_to_updated_onto = path_to_save + "fuskg-multimodal-{}_complete.ttl".format(dataset)
    connect_mdr(onto_mm, fsreci_ns, fsmumo_ns, modality_node_instances, recipes_info, metadata, path_to_updated_onto, dataset)

