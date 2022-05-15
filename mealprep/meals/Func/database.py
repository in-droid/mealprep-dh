from meals.models import *

class DataBase:
    def __init__(self):
        pass

    # Returns all Foods
    def get_foods(self):
        return Foods.objects.all()

    # Returls all Foods
    def get_recipes(self):
        return Recipes.objects.all()

    # Returns all Uer_Fridge entries for specific user by UID (if uid is not found, returns None)
    def get_fridge(self, uid):
        try:
            return User_Fridge.objects.filter(uid=uid)
        except:
            return None

    # Return all food names from fridge for specific user ID
    def get_food_names_from_fridge(self, uid):
        try:
            return User_Fridge.objects.filter(uid=uid)
        except:
            return None

    def get_food_for_id(self, fid):
        try:
            return Foods.objects.get(id=fid)
        except:
            return None

    # Get ingridients for a Recipes ID
    def get_ingridients(self, id):
        try:
            return  Recipes.objects.get(id=id).ingridients
        except:
            return None

    # Add to Foods with input (name, volume), and optinal arguments (calories, protein)
    def add_to_foods(self, name, type, calories=None, protein=None):
        Foods(name=name, type=type, calories=calories, protein=protein).save()
        
    # Add to Fridge with input (user_id, food_id, volume)
    def add_to_fridge(self, uid, fid, volume):
        User_Fridge(uid=uid, fid=fid, volume=volume).save()
        
    # Add to Recipes with input (name, directions, ingridients, type) and optional arguments (time, image)
    def add_to_recipes(self, name, directions, ingridients, type, time=None, image=None):
        Recipes(name=name, directions=directions, ingridients=ingridients, type=type, time=time, image=image).save()
        
    # Update User_Fridge with input (user_id, food_id, new_volume)
    def update_fridge(self, uid, fid, new_volume):
        User_Fridge.objects.filter(uid=uid, fid=fid).update(volume=new_volume)