import json

from pathlib import Path

import pandas as pd

# Load the champion data from the project's Raw_Data directory.
data_path = Path('../../Raw_Data/League_of_Legends.json')
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

STATS=['stats.hpperlevel','hp', 'stats.mp', 'stats.mpperlevel',
       'move_speed', 'stats.armor', 'stats.armorperlevel', 'stats.spellblock',
       'stats.spellblockperlevel', 'stats.attackrange', 'stats.hpregen',
       'stats.hpregenperlevel', 'stats.mpregen', 'stats.mpregenperlevel',
       'stats.crit', 'stats.critperlevel', 'attack_damage',
       'stats.attackdamageperlevel', 'stats.attackspeedperlevel',
       'stats.attackspeed']

role_analysis= ['name']+ AINFO + STATS
scaling_analysis=AINFO
correlation_analysis=AINFO
oop_csv=AINFO
ROLS_ANALYSIS_CSV=champions[role_analysis]

SCALING_ANALYSIS_CSV=champions[scaling_analysis]

CORRELATION_ANALYSIS_CSV=champions[correlation_analysis]

OOP_CSV =champions[oop_csv]

All_Csv = {
    'Rols_Analysis.csv':        ROLS_ANALYSIS_CSV,
    'Scaling_Analysis.csv':     SCALING_ANALYSIS_CSV,
    'Correlation_Analysis.csv': CORRELATION_ANALYSIS_CSV,
    'OOP.csv':                  OOP_CSV,
}
for Csv_file_name,Data_to_Csv in All_Csv.items():
    csv_path = Path(fr'../Raw_Data/{Csv_file_name}')
    Data_to_Csv.to_csv(csv_path, index=False, encoding='utf-8-sig')

# A final expression is rendered as the notebook cell's visible table output.
# print(ROLS_ANALYSIS_CSV)
# print(champions.columns)

