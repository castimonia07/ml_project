import os #for generic code writting as it will give the path of folder in generic way
from pathlib import Path # for generic code writting as it will give the path of folder in generic way
import logging

logging.basicConfig(level=logging.INFO)

project_name="ml_project"

# list of files ye btate hai ki hame apne project me kon konse files chahiye 
list_of_files=[
    ".github/workflows/.gitkeep" # ye sihliye bnaya hai kyuki hme deployment ke time pe github actions likhne padte hai to uske liye ye bnaya hai
    f"src/{project_name}/__init__.py", # ye isliye bnaya hai kyuki jab bhi ham apne project ko package me convert krte hai to uske andar __init__.py file honi chahiye tabhi wo package ke roop me kaam karega
    f"src/{project_name}/components/__init__.py", # ye isliye bnaya hai kyuki jab bhi ham apne project ko package me convert krte hai to uske andar __init__.py file honi chahiye tabhi wo package ke roop me kaam karega
    f"src/{project_name}/components/data_ingestion.py", # ye isliye bnaya hai kyuki hamare project me data ingestion ka component hai to uske liye ye file bnaya hai
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/pipelines/__init__.py", 
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/pipelines/testing_pipelines.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")
    
    if not os.path.exists(filepath) or (os.path.getsize(filepath)==0):    
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")
    
    else:
        logging.info(f"{filename} already exists")











