import json
from pathlib import Path

import pandas as pd

#Calculate Notebooks path from the src folder

data_path = Path("../Raw_Data/League_of_Legends.json")
with data_path.open(encoding="utf-8") as file:
    raw_data = json.load(file)

# Riot JSON-də çempionların məlumatı data sahəsinin içindədir.
champions = pd.json_normalize(raw_data["data"].values())

print(champions.head(10))