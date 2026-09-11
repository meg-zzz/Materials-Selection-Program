import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

from mp_api.client import MPRester
with MPRester(API_KEY) as mpr:

# Selecting data to retrieve from Materials Project API in materials.summary
    data = mpr.materials.summary.search(
        material_ids="mp-1047",
        fields=["young_modulus"],
    )

print(data)