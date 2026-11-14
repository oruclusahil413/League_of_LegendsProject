import json
from pathlib import Path

import pandas as pd

# Load the champion data from the project's Raw_Data directory.
data_path = Path('../Raw_Data/League_of_Legends.json')
with data_path.open(encoding='utf-8') as file:
    raw_data = json.load(file)

# The champion records live under the JSON document's data field.
champions = pd.json_normalize(raw_data['data'].values()).rename(
    columns={
        'info.attack': 'attack',
        'info.defense': 'defense',
        'info.magic': 'magic',
        'info.difficulty': 'difficulty',
        'stats.hp': 'hp',
        'stats.movespeed': 'move_speed',
        'stats.attackdamage': 'attack_damage',
    }
)

output_columns = [
              'id', 'name',
              'title', 'tags',
               'attack', 'defense',
               'magic', 'difficulty',
               'hp', 'move_speed', 'attack_damage',
]
preview = champions[output_columns].head(10)

csv_path = Path('League_of_Legends.csv')
champions.to_csv(csv_path, index=True, encoding='utf-8-sig')

print(f'Champion count: {len(champions)}')
print(f'CSV saved: {csv_path.resolve()}')

# A final expression is rendered as the notebook cell's visible table output.
print(preview)

