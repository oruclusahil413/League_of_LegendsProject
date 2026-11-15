import json

from pathlib import Path

import pandas as pd

# Load the champion data from the project's Raw_Data directory.
data_path = Path('../Raw_Data/League_of_Legends.json')
with data_path.open(encoding='utf-8') as file:
    raw_data = json.load(file)

# The champion records live under the JSON document's data field.
CHAMPDATA= pd.json_normalize(raw_data['data'].values())

champions=CHAMPDATA.rename(
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

INFO=['version', 'id', 'key', 'name']

IMAGE=['image.full','image.sprite',
       'image.group', 'image.x',
       'image.y', 'image.w',
       'image.h']

TAGS=['tags']
BLURB_TITLE=['blurb','partype','title']
AINFO=['attack', 'defense', 'magic', 'difficulty']

STATS=['stats.hpperlevel', 'stats.mp', 'stats.mpperlevel',
       'move_speed', 'stats.armor', 'stats.armorperlevel', 'stats.spellblock',
       'stats.spellblockperlevel', 'stats.attackrange', 'stats.hpregen',
       'stats.hpregenperlevel', 'stats.mpregen', 'stats.mpregenperlevel',
       'stats.crit', 'stats.critperlevel', 'attack_damage',
       'stats.attackdamageperlevel', 'stats.attackspeedperlevel',
       'stats.attackspeed']

ROLS_ANALYSIS_CSV=[]

SCALING_ANALYSIS_CSV=[]

CORRELATION_ANALYSIS_CSV=[]

OOP_CSV=[]

preview = champions.head(10)

csv_path = Path(r'../Raw_Data/League_of_Legends.csv')
champions.to_csv(csv_path, index=True, encoding='utf-8-sig')

print(f'Champion count: {len(champions)}')
print(f'CSV saved: {csv_path.resolve()}')

# A final expression is rendered as the notebook cell's visible table output.
print(preview)
print(champions.columns)

