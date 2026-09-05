#setup to retrieve API key from .env file
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

import pandas as pd

#Importing Materials Project API
from mp_api.client import MPRester
with MPRester(API_KEY) as mpr:

#Selecting data to retrieve from Materials Project API in materials.summary
    data = mpr.materials.summary.search(
        fields=[
            'material_id',
            'formula_pretty',
            'composition_reduced',
            'density',
            'bulk_modulus',
            'shear_modulus',
            'homogeneous_poisson',
            'band_gap',
            'is_stable',
            'is_magnetic']
    )
#create python dictionary
[mat.dict() for mat in data]