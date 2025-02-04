# Abox recipes generation

Scripts for processing and linking recipe data, including recipes' names, preparation steps, ingredients, nutrients, and multi-modal information (images/videos) of Recipe1M and Tasty dataset.  

## Prerequisites

Before running any script, ensure that you have created the `.pkl` file for recipes (Recipe1M+ and Tasty).  
Therefore the first script to execute is: `OnlyRecipesSteps/populate_ontology_with_steps.py`

Then follow the steps below in order to correctly create the corresponding ABox.

### 1. Generate Recipe Labels

`OnlyRecipesSLabels/populate_ontology_recipes_labels.py`: This script creates `.ttl` files containing only the names (labels) of recipes (e.g., Lasagne, Pasta with Beans, etc.).

### 2. Connect Recipes with Preparation Steps

`OnlyRecipes/connect_recipes_with_step.py`: This script links the recipe labels with their corresponding preparation steps.

### 3. Connect Recipes with Ingredients and Nutrients

`USDARecipes/connect_rin.py`: This script associates recipes from the Recipe1M+ dataset with their ingredients and nutritional information.

### 4. Link Recipes with Multi-modal Information 

`ConnectMultiModalInfo/connect_multimodality.py`: This script connects recipes with their respective images or videos.

> **⚠️ Important**
> 
> - Refer to the help arguments inside each script to ensure correct execution (e.g., setting file paths, choosing the dataset to process).
> 
> - `ConnectMultiModalInfo/connect_multimodality.py` before running the script, make sure to unzip Metadata.rar and update the corresponding file paths in the script.

---

If you encounter any issues, feel free to reach out.
