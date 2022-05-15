from meals.Func.database import DataBase
import pandas as pd
import sys
from meals.models import *

db = DataBase()

import os
os.chdir('/home/radoslav/Desktop/dragonhack/mealprep-dh/mealprep/meals/Func/data/')
# print()
# print(sys.path)
# print('-----------------------------')
def add_foods():
    df = pd.read_csv('data_clean.csv')
    # print("HERE <<<<<<<<<<<<")
    for name, type, calories, protein in df[['name', 'Food Group', 'Calories', 'Protein (g)']].values:
        # print(name, type, calories, protein)
        # print("=========================")
        db.add_to_foods(name, type, calories, protein)
        # Foods(name=name, type=type, calories=calories, protein=protein).save()
add_foods()