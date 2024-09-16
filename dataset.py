import zipfile
import os
import shutil
from pathlib import Path

os.environ['KAGGLE_USERNAME'] = 'YOUR_USER_NAME'
os.environ['KAGGLE_KEY'] = 'YOUR_API_KEY'

if not os.path.exists("./plantvillage-dataset") or not os.path.exists("./plantvillage-dataset.zip"):
    # Download the dataset from Kaggle if it hasn't been downloaded yet
    os.system("kaggle datasets download -d abdallahalidev/plantvillage-dataset")

if os.path.exists("./plantvillage-dataset.zip"):
    # Extract the zip file to the specified directory
    with zipfile.ZipFile("./plantvillage-dataset.zip", 'r') as zip_ref:
        zip_ref.extractall('./plantvillage-dataset')

    os.remove("./plantvillage-dataset.zip")

