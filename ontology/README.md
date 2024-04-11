# Modules

## Content

### TBox
- **mumonut-tbox.ttl:** Contains the TBox of MuMoNut.
- **helis-v1.14-foodonly-tbox.ttl:** Contains the TBox of Helis, including relevant concepts.
- **ontology-usda-v1.0-tbox.ttl:** Contains the TBox of USDA ingredients and nutrients.

### ABox
- **helis-v1.14-foodonly.ttl:** ABox of Helis populated with its list of recipes (i.e., RecipeDB and Turconi).
- **usda-ontology-v1.0.ttl:** ABox of the USDA ontology, populated with its ingredients and nutrients.
- **recipes-usda-food-recipe1m.ttl:** Contains, for each recipe of Recipe1m+, its corresponding USDA ingredients and nutrients.
- **recipe-labels-recipe1m.ttl:** Contains recipes’ names of Recipe1m+.
- **recipe-labels-tasty.ttl:** Contains recipes’ names of Tasty.
- **description-steps.ttl:** Contains description steps.
- **recipes-recipe-steps-recipe1m.ttl:** Contains, for each recipe of Recipe1m+, its corresponding recipe steps.
- **recipes-recipe-steps-tasty.ttl:** Contains, for each recipe of Tasty, its corresponding recipe steps.
- **mm-entities-recipe1m.ttl:** Contains, for each recipe of Recipe1m+, its corresponding multimodal resources (i.e., images URL).
- **mm-entities-Tasty.ttl:** Contains, for each recipe of Tasty, its corresponding multimodal resources (i.e., path to video inside the zipped folder).

## Loading Ontologies

Loading the FuS-KG Modules requires specific dependencies:

- Loading of `mumonut-tbox.ttl` requires `helis-v1.14-foodonly-tbox.ttl` and `ontology-usda-v1.0-tbox.ttl`.
- Loading of `recipes-usda-food-recipe1m.ttl`, `recipe-labels-recipe1m.ttl`, `recipe-labels-tasty.ttl`, `description-steps.ttl`, `recipes-recipe-steps-recipe1m.ttl`, `recipes-recipe-steps-tasty.ttl`, `mm-entities-recipe1m.ttl`, and `mm-entities-tasty.ttl` requires `helis-v1.14-foodonly.ttl` and `usda-ontology-v1.0.ttl`.

Alternatively, you can load all files except `recipes-usda-food-recipe1m.ttl` (for
which you need the data coming from `usda-ontology-v1.0.ttl`) faster using `helis-v1.14-foodonly-tbox.ttl` and `ontology-usda-v1.0-tbox.ttl`.

## Note

Ensure that the appropriate dependencies are resolved for the correct loading and utilization of the FuS-KG Modules