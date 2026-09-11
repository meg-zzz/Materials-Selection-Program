#setup to retrieve API key from .env file
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

from pymatgen.core import Element
import pandas as pd

element_optns = [el.symbol for el in Element]

#Ask user for element requirements
while True:
    E = input("Elements needed separated by commas (eg. Fe, C): ").split(',')
    user_elements = [element.strip() for element in E]
    if all(element in element_optns for element in user_elements):
        break
    else:
        print('Invalid element entered, please try again. Remember to separate with commas and to capitalise first letter.')

field_optns = ['density',
            'bulk_modulus',
            'shear_modulus',
            'homogeneous_poisson',
            'band_gap',
            'is_magnetic']

#Importing Materials Project API
from mp_api.client import MPRester
with MPRester(API_KEY) as mpr:

#Selecting data to retrieve from Materials Project API in materials.summary
    data = mpr.materials.summary.search(
        elements = user_elements,
        fields = field_optns + ['material_id', 'formula_pretty', 'composition_reduced', 'is_stable']
        )

#Create python dictionary
D = [mat.dict() for mat in data]

#Create a pandas data frame with data from the dictionary
df = pd.DataFrame(D)

print(f'{len(df)} materials found.')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
print(df.head())