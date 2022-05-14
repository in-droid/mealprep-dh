from meals.models import *
from meals.Func.database import DataBase

import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer

class Recommender:
    def __init__(self, uid):
        self.uid = uid
        self.db = DataBase()
        self.lemmatizer = WordNetLemmatizer()

    def _lemmatize_word(self, word):
        return self.lemmatizer.lemmatize(word.lower())

    def _lemmatize_ingridients(self, ingridients):
        return {self._lemmatize_word(key): value for key, value in ingridients.items()}

    def recommend(self):
        all_recipes = self.db.get_recipes()
        # all_fridge = self.db.get_fridge(uid=self.uid)
        for recipe in all_recipes:
            print(self.db.get_ingridients(recipe.id))

        print(self.db.get_food_names_from_fridge(self.uid))
        # for food in all_fridge:
        #     print(self.get_food_names_from_fridge())
        # print(all_recipes)
        # print(all_fridge)



# Recommender()