from meals.models import *
from meals.Func.database import DataBase

import ast
import numpy as np
# import tqdm
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

    # def _lemmatize_ingridients(self, ingridients):
        # return {self._lemmatize_word(key): value for key, value in ingridients.items()}

    def recommend(self):
        # to_arr = lambda x: [ast.literal_eval(y) for y in x]
        foods_arr = self.db.get_food_names_from_fridge(self.uid)

        recipes_arr = []
        for recipe in self.db.get_recipes():
            # ingrediants_arr.append(self.db.get_ingridients(recipe.id))
            ingridiants = self.db.get_ingridients(recipe.id)
            # print("======================================")
            P = self.get_probability(ast.literal_eval(ingridiants).keys(), foods_arr)
            recipes_arr.append((recipe, P))
        print(sorted(recipes_arr, key=lambda x: x[1], reverse=True)[:5])

    def get_probability(self, recipe, fridge):
        P = 0
        # c = 0
        for item in recipe:
            tokens = nltk.word_tokenize(item)
            N1 = self.getNouns(tokens)
            V1 = self.getVerbs(tokens)
            A1 = self.getAdjs(tokens)
            PNs = []
            PAVs = []
            PX = []
            # c += 1
            for food in fridge:
                tokens2 = nltk.word_tokenize(food)
                N2 = self.getNouns(tokens2)
                V2 = self.getVerbs(tokens2)
                A2 = self.getAdjs(tokens2)
                p1 = len(np.intersect1d(N1, N2))
                p2 = len(np.union1d(N1, N2))
                if p2 != 0:
                    pn = p1 / p2
                    # PNs.append(((p1 / p2), food))
                else:
                    pn = 0
                    # PNs.append((0, food))
                p1 = np.union1d(A1, V1)
                p2 = np.union1d(A2, V2)
        
                PNs.append((pn, food))
                PAVs.append(((len(np.intersect1d(p1, p2))+1) / (len(np.union1d(p1, p2))+2), food))
                PX.append(pn * (len(np.intersect1d(p1, p2))+1) / (len(np.union1d(p1, p2))+2))

            # if np.sum([1 for x in PX if x > 0]) == len(fridge):
            # if max(PX) != 0:
                # c+=1
            P+=np.sum(PX)
        # print(c, len(recipe))
        return P