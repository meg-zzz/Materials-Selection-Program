#Setup to retrieve API key from .env file
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

#Import elements to double check user input of required elements
from pymatgen.core import Element

#Import pandas for creation of DataFrame
import pandas as pd

element_optns = [el.symbol for el in Element]

#Define element requirements with user input
while True:
    E = input("Elements needed separated by commas (eg. Fe, C): ").split(',')
    user_elements = [element.strip() for element in E]
    if all(element in element_optns for element in user_elements):
        break
    else:
        print('Invalid element entered, please try again. ' \
        'Remember to separate with commas and capialise first letter.')

#Define fields to be extrated from API
field_optns = ['density',
            'bulk_modulus',
            'shear_modulus',
            'homogeneous_poisson',
            'band_gap',
            'is_magnetic',
            'is_stable']

#Importing Materials Project API
from mp_api.client import MPRester
with MPRester(API_KEY) as mpr:

#Selecting data to retrieve from Materials Project API in materials.summary 
# with previously defined elements and fields
    data = mpr.materials.summary.search(
        elements = user_elements,
        fields = field_optns + ['material_id', 'formula_pretty', 
                                'composition_reduced', 'warnings']
        )

#Create python dictionary
D = [mat.dict() for mat in data]

#Create a pandas DataFrame with data from the dictionary
df = pd.DataFrame(D)

#Printing length of DataFrame to inform user of available materials
print(f'{len(df)} materials found.')

#Creating new columns with the three types of bulk moduli provided by the API
df['voigt_bulk'] = df['bulk_modulus'].apply(lambda x: x['voigt'] if x is not None else None)
df['reuss_bulk'] = df['bulk_modulus'].apply(lambda x: x['reuss'] if x is not None else None)
df['vrh_bulk'] = df['bulk_modulus'].apply(lambda x: x['vrh'] if x is not None else None)

#Creating new columns with the three types of shear moduli provided by the API
df['voigt_shear'] = df['shear_modulus'].apply(lambda x: x['voigt'] if x is not None else None)
df['reuss_shear'] = df['shear_modulus'].apply(lambda x: x['reuss'] if x is not None else None)
df['vrh_shear'] = df['shear_modulus'].apply(lambda x: x['vrh'] if x is not None else None)