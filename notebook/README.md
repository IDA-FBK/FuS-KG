# Running the Google Colab Notebook

This README will guide you through the process of loading and running the Google Colab notebook provided in this repository.

## Table of Contents

1. [Loading and running the Notebook from GitHub](#loading-from-github)
2. [Running the Notebook locally on Colab](#running-locally-on-colab)

## Loading the Notebook from GitHub

To load and run the notebook directly from GitHub:

1. **Open Google Colab**: Go to [Google Colab](https://colab.research.google.com/).
2. **GitHub Tab**: Click on the `GitHub` tab in the welcome window or select `File > Open notebook > GitHub` from the menu.
3. **Authorize GitHub**: If you haven't already, authorize Google Colab to access your GitHub account.
4. **Search for the Notebook**: In the search bar, type `https://github.com/IDA-FBK/FuS-KG/tree/main/notebook` and click the search lens icon on the right.
5. **Select the Notebook**: Select `notebook/CQs-colab.ipynb` file.
6. **Run the Notebook**: Once the notebook is open, you can run the cells by clicking on the play button next to each cell.



## Running the Notebook Locally on Colab

If you have downloaded the notebook to your local machine and want to run it on Colab:

1. **Open Google Colab**: Go to [Google Colab](https://colab.research.google.com/).
2. **File Upload**: Click on `File > Upload notebook` from the menu.
3. **Upload the Notebook**: Choose the `.ipynb` file from your local disk and upload it.
4. **Run the Notebook**: Once uploaded, the notebook will open in Colab and you can run the cells as usual.

### Notes
- Make sure you have a stable internet connection.
- If you need to install any dependencies, make sure to run the appropriate setup cells first.
- You can also modify the code and rerun the cells as needed.

## ⚙️Troubleshooting

#### Memory Issue on Free Colab Accounts

Free Colab accounts provide approximately 12GB of RAM (CPU). When loading large graphs, you might encounter this error:

> "Your session crashed after using all available RAM."

This indicates the session ended due to exceeding all the available RAM memory. To resolve this:

1. Run the setup cell (the first cell in the notebook), followed by the cell that caused the error.
2. If the problem persists, go to `Runtime > Restart runtime`, then rerun the setup cell, followed by the cell that caused the error.

💡 **Tip**: For additional memory, consider upgrading to a Colab Pro account.
