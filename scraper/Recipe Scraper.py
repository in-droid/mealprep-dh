import requests
from bs4 import BeautifulSoup
from fractions import Fraction

class Recipe:
    def __init__(self, name, directions, ingredients, type, image):
        self.name = name
        self.directions = directions
        self.ingredients = ingredients
        self.type = type
        self.image = image

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
            quantityText = ingredientLI.find('span', {'class': 'recipe__list-qty'}).find('span').text.strip()
            quantity = float(sum(Fraction(s) for s in quantityText.split()))
            measurement = ingredientLI.find('span', {'class': 'recipe__list-qty'}).contents[2].strip().lower()
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
            quantity = round(quantity, 1)
            ingredient = ingredientLI.contents[1]
            ingredientDict[ingredient] = (quantity, measurement)

    directions = soup.find('div', {'id': 'recipeDirectionsRoot'}).text.strip()
    directions = "".join([s for s in directions.splitlines(True) if s.strip("\r\n")])

    return name, directions, type, ingredientDict



print(scrapeRecipePage('https://food52.com/recipes/4560-goat-cheese-caesar-salad-with-roasted-tomatoes-and-parmesan-crisp','dinner'))




