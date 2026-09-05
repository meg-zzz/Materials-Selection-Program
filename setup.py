import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

from mp_api.client import MPRester
with MPRester(API_KEY) as mpr:

    docs = mpr.materials.summary.search(
        elements=["Fe", "Ni", "Cr"]
    )
doc = docs[0]

for result in doc:
    print(result)