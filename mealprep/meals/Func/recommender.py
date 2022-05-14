from meals.models import *
from meals.Func.database import DataBase

import ast
# import json
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')



from nltk.stem import WordNetLemmatizer

class Recommender:
    def __init__(self, uid):
        self.uid = uid
        self.db = DataBase()
        self.lemmatizer = WordNetLemmatizer()


    def getNouns(self, tokens):
        is_noun = lambda pos: pos[:2] == 'NN'
        return [self._lemmatize_word(item) for (item, pos) in nltk.pos_tag(tokens) if is_noun(pos)]

    def getVerbs(self, tokens):
        is_verb = lambda pos: pos[:2] == 'VB'
        return [self._lemmatize_word(item) for (item, pos) in nltk.pos_tag(tokens) if is_verb(pos)]

    def getAdjs(self, tokens):
        is_adj = lambda pos: pos[:2] == 'JJ'
        return [self._lemmatize_word(item) for (item, pos) in nltk.pos_tag(tokens) if is_adj(pos)]

    def _lemmatize_word(self, word):
        return self.lemmatizer.lemmatize(word.lower())

    def _lemmatize_ingridients(self, ingridients):
        return {self._lemmatize_word(key): value for key, value in ingridients.items()}

    def recommend(self):
        # to_arr = lambda x: [ast.literal_eval(y) for y in x]
        foods_arr = self.db.get_food_names_from_fridge(self.uid)

        ingrediants_arr = []
        for recipe in self.db.get_recipes():
            # ingrediants_arr.append(self.db.get_ingridients(recipe.id))
            ingridiants = self.db.get_ingridients(recipe.id)
            self.get_probability(ast.literal_eval(ingridiants).keys(), foods_arr)
            # print(ingridiants)

            # print(self.db.get_ingridients(recipe.id))

        # foods_arr = self.db.get_food_names_from_fridge(self.uid)
        
        # # print(ingrediants_arr)
        # # print(foods_arr)

        # print('---------------------------')
        # for d in ingrediants_arr:
        #     arr = []
        #     # tokens = []
        #     # print(ast.literal_eval(d))
        #     for key, val in ast.literal_eval(d).items():
        #         arr.append(key)
        #         tokens = nltk.word_tokenize(key)
        #         print(self.getNouns(tokens), self.getVerbs(tokens), self.getAdjs(tokens))
        #     # print(arr)


        #     break
        
        # print(to_arr())
    print("-----------")

    def get_probability(self, recipe, fridge):
        print(recipe)
        print(fridge)
        for item in recipe:
            tokens = nltk.word_tokenize(item)
            print(tokens)
        # print("-----------")
        # print(nltk.word_tokenize(recipe))

