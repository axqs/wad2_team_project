import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad2_team_project.settings')
import django
django.setup()
from recipes.models import *
from django.contrib.auth.models import User

cat_objects = {}
admin_objects = {}
def populate():
    reviews = {"Best pancakes" : {"author" : "q_smart", "recipe" : "Pancakes", "chef" : "lynda_faller", "rating" : 4.25}
    }
    admins = {
        "lynda_faller" : {"email":"lynda@gmail.com", "password":"lyndafaller", "fname":"Lynda", "lname":"Faller", "chef":True},
        "amy_hynes" : {"email":"amy@gmail.com", "password":"amyhynes", "fname":"Amy", "lname":"Hynes", "chef":True},
        "eve_ohagan" : {"email":"eve@gmail.com", "password":"eveohagan", "fname":"Eve", "lname":"O'Hagan", "chef":True},
        "q_smart" : {"email":"q@gmail.com", "password":"qiufeismart", "fname":"Q", "lname":"Smart", "chef":True},}
    breakfast_recipes = [
        {"name": "Pancakes",
         "cook_time" : 15,
         "cats" : "Breakfast, American",
         "chef": "lynda_faller",
         },]
    lunch_recipes = [
        {"name": "Chicken Pesto Panini",
         "cook_time" : 10,
         "cats" : "Lunch, American",
         "chef": "eve_ohagan",
         },]
    dinner_recipes = [
        {"name": "All-American Burger",
         "cook_time" : 25,
         "cats" : "Dinner, American",
         "chef": "q_smart",
         },]
    dessert_recipes = [
        {"name": "Traditional Tiramisu",
         "cook_time" : 30,
         "cats" : "Dessert, Italian",
         "chef": "amy_hynes",
         },]
    special_recipes = [
        {"name": "St Paddy's Shake",
         "cook_time" : 35,
         "cats" : "Special Occasions, Dessert",
         "chef": "eve_ohagan",
         },]
    italy_recipes = [
        {"name": "Spaaghetti Carbonara",
         "cook_time" : 35,
         "cats" : "Dinner, Italian",
         "chef": "amy_hynes",
         },]
    usa_recipes = [
        {"name": "Classic Hot Dogs",
         "cook_time" : 30,
         "cats" : "Lunch, American",
         "chef": "lynda_faller",
         },]
    mex_recipes = [
        {"name": "Old School Beef Tacos",
         "cook_time" : 30,
         "cats" : "Dinner, Mexican",
         "chef": "amy_hynes",
         },]
    china_recipes = [
        {"name": "Easy Chicken Chow Mein",
         "cook_time" : 40,
         "cats" : "Dinner, Chinese",
         "chef": "lynda_faller",
         },]
    india_recipes = [
        {"name": "Chicken Curry",
         "cook_time" : 45,
         "cats" : "Dinner, Indian",
         "chef": "eve_ohagan",
         },]
    japan_recipes = [
        {"name": "California Rolls",
         "cook_time" : 50,
         "cats" : "Lunch, Japanese",
         "chef": "q_smart",
         },]
    cuisines = {"Italian": {"recipes": italy_recipes, "likes": 64 },
            "American": {"recipes": usa_recipes, "likes": 32 },
            "Mexican": {"recipes": mex_recipes, "likes": 16 },
            "Chinese": {"recipes": china_recipes, "likes": 16 },
            "Indian": {"recipes": india_recipes, "likes": 16 },
            "Japanese": {"recipes": japan_recipes, "likes": 16 },}

    cats = {"Breakfast": {"recipes": breakfast_recipes, "likes": 64 },
            "Lunch": {"recipes": lunch_recipes, "likes": 32 },
            "Dinner": {"recipes": dinner_recipes, "likes": 16 },
            "Dessert": {"recipes": dessert_recipes, "likes": 16 },
            "Cuisines": cuisines,
            "Special Occasions": {"recipes": special_recipes, "likes": 16 },}

    for admin, admin_data in admins.items():
        u = add_user(admin,admin_data)
        admin_objects[admin] = u

    for cat, cat_data in cats.items():
        if(cat == "Cuisines"):
            c = add_cat(cat, 0, 'CAT', None)
            cat_objects[cat] = c
            for cuisine, cuisine_data in cuisines.items():
                sc = add_cat(cuisine, cuisine_data["likes"], 'SUB', c)
                cat_objects[cuisine] = sc
        else:
            c = add_cat(cat,cat_data["likes"], 'CAT', None)
            cat_objects[cat] = c

    for cat, cat_data in cats.items():
        if(cat == "Cuisines"):
            for subcat, subcat_data in cat_data.items():
                for r in subcat_data["recipes"]:
                    add_recipe(r["cats"], r["name"], r["cook_time"], r["chef"])
        else:
            for r in cat_data["recipes"]:
                add_recipe(r["cats"], r["name"], r["cook_time"], r["chef"])

    for review, review_data in reviews.items():
        r = add_review(review,review_data)

def add_recipe(cats_lst, name, cook_time, chef):
    r = Recipe.objects.get_or_create(chef=admin_objects[chef], name=name)[0]
    r.name = name
    r.cook_time = cook_time
    cats_lst = cats_lst.split(", ")
    print(name,cats_lst)
    for c in cats_lst:
        r.categories.add(cat_objects[c])
    r.save()
    return r

def add_cat(name, likes, type, supercat):
    if type == 'SUB':
        c = Category.objects.get_or_create(name=name, type=type, supercat=supercat)[0]
    else:
        c = Category.objects.get_or_create(name=name, type=type)[0]
    c.likes=likes
    c.save()
    return c

def add_user(username, user_data):
    user = User.objects.get_or_create(username=username)[0]
    user.email = user_data["email"]
    user.set_password(user_data["password"])
    user.first_name = user_data["fname"]
    user.last_name = user_data["lname"]
    user.is_staff = True
    user.save()
    if(user_data["chef"]):
        add_chef(user, user.username, user.first_name, user.last_name, user.email)
    return user

def add_chef(user,username,fname,lname,email):
    chef = Chef.objects.get_or_create(user=user)[0]
    chef.username = username
    chef.fname = fname
    chef.lname = lname
    chef.email = email
    chef.save()
    return chef

def add_review(title,review_data):
    recipe_chef = review_data["chef"]
    recipe_name = review_data["recipe"]
    author = review_data["author"]
    rating = review_data["rating"]

    recipe = Recipe.objects.get(chef=admin_objects[recipe_chef], name=recipe_name)
    chef = Chef.objects.get(user=admin_objects[author])
    review = Review.objects.get_or_create(recipe=recipe, author=chef)[0]
    review.title = title
    review.rating = review_data["rating"]
    review.save()
    return review

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
