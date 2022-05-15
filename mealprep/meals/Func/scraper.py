import requests
from bs4 import BeautifulSoup
from fractions import Fraction
from meals.Func.database import DataBase

db = DataBase()

def scrapeRecipePage(URL, type):

    cupList = ['cup', 'cups']
    tbspList = ['tablespoon', 'tablespoons', 'tbsp', 'tbsp.']
    tspList = ['teaspoon', 'teaspoons', 'tsp', 'tsp.']
    pinchList = ['pinch']
    ounceList = ['ounce', 'ounces', 'oz', 'oz.']
    mlList = ['milliliter', 'milliliters', 'millilitre', 'millilitres', 'ml', 'ml.']
    literList = ['liter', 'liters', 'litre', 'litres', 'l', 'l.']
    gramList = ['gram', 'grams', 'g', 'g.']
    galList = ['gallon', 'gallons', 'gal', 'gal.']
    poundList = ['pound', 'pounds', 'lb', 'lb.']
    kiloList = ['kilogram', 'kilograms', 'kg', 'kg.']
    quartList = ['qt', 'qt.', 'quart', 'quarts']
    pintList = ['pint', 'pints', 'pt', 'pt.']

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    name = soup.find('h1', {'class': 'recipe__title'}).text.strip()

    ingredientDict = dict()

    ingredientULs = soup.find('div', {'class' : 'recipe__list recipe__list--ingredients'}).findAll('ul')

    for ingredientUL in ingredientULs:
        ingredientLIs = ingredientUL.select('li:not(.recipe__list-subheading)')
        for ingredientLI in ingredientLIs:
            try:
                quantityText = ingredientLI.find('span', {'class': 'recipe__list-qty'}).find('span').text.strip()
                quantity = float(sum(Fraction(s) for s in quantityText.split()))
                measurement = ingredientLI.find('span', {'class': 'recipe__list-qty'}).contents[2].strip().lower()
            except:
                quantity = ""
                measurement = ""
            if measurement in cupList:
                quantity = 128 * quantity
                measurement = 'g'
            elif measurement in tbspList:
                quantity = 14 * quantity
                measurement = 'g'
            elif measurement in tspList:
                quantity = 5 * quantity
                measurement = 'g'
            elif measurement in pinchList:
                measurement = 'pinch'
            elif measurement in ounceList:
                quantity = 28 * quantity
                measurement = 'g'
            elif measurement in mlList:
                measurement = 'g'
            elif measurement in literList:
                quantity = 1000 * quantity
                measurement = 'g'
            elif measurement in gramList:
                measurement = 'g'
            elif measurement in galList:
                quantity = 3700 * quantity
                measurement = 'g'
            elif measurement in poundList:
                quantity = 450 * quantity
                measurement = 'g'
            elif measurement in kiloList:
                quantity = 1000 * quantity
                measurement = 'g'
            elif measurement in pintList:
                quantity = 470 * quantity
                measurement = 'g'
            elif measurement in quartList:
                quantity = 940 * quantity
                measurement = 'g'
            if quantity != "":
                quantity = round(quantity, 1)
            ingredient = ingredientLI.contents[1]
            ingredientDict[ingredient.strip('\n')] = (quantity, measurement)

    directions = soup.find('div', {'id': 'recipeDirectionsRoot'}).text.strip()
    directions = "".join([s for s in directions.splitlines(True) if s.strip("\r\n")])

    imgLink = soup.find('div', {'class': 'img'}).find('img')['data-pin-media']

    db.add_to_recipes(name, directions, ingredientDict, type, None, imgLink)


def scrapeRecipes(URL, type):

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    recipes = soup.find('div', {'class': 'recipe-results'}).findAll('div', {'class': 'card collectable'})
    for recipe in recipes:
        link ="https://food52.com" + recipe.find('a')['href'].strip()
        scrapeRecipePage(link, type)


scrapeRecipes('https://food52.com/recipes/breakfast', 'breakfast')
scrapeRecipes('https://food52.com/recipes/lunch', 'lunch')
scrapeRecipes('https://food52.com/recipes/dinner', 'dinner')
scrapeRecipes('https://food52.com/recipes/salad', 'salad')

