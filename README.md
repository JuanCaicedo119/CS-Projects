This is a Rest API developed with Python framework FastAPI that performs CRUD operations on data.
The data is locally stored using Mongo Data Base and takes the form of a 'user' with fields name, email, and password.
User password is encrypted with SHA-256 using python library passlib.hash

Requirements to run locally:
1. MongoDB Community Server version 5.0.6 or later
2. Python version 3.0 or later
3. Python packages: fastAPI, uvicorn, pymongo, passlib

To RUN: 
Inside folder, run cdm: uvicorn app:app --reload
