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
    recipes = [
        {"name": "Pancakes",
         "cook_time" : 15,
         "cats" : "Breakfast, American",
         "chef": "lynda_faller",
         },
        {"name": "Chicken Pesto Panini",
         "cook_time" : 10,
         "cats" : "Lunch, American",
         "chef": "eve_ohagan",
         },
        {"name": "All-American Burger",
         "cook_time" : 25,
         "cats" : "Dinner, American, 4th of July",
         "chef": "q_smart",
         },
        {"name": "Traditional Tiramisu",
         "cook_time" : 30,
         "cats" : "Dessert, Italian",
         "chef": "amy_hynes",
         },
        {"name": "St Paddy's Shake",
         "cook_time" : 35,
         "cats" : "Special Occasions, Dessert, St Patrick's Day",
         "chef": "eve_ohagan",
         },
        {"name": "Spaaghetti Carbonara",
         "cook_time" : 35,
         "cats" : "Dinner, Italian",
         "chef": "amy_hynes",
         },
        {"name": "Classic Hot Dogs",
         "cook_time" : 30,
         "cats" : "Lunch, American, 4th of July",
         "chef": "lynda_faller",
         },
        {"name": "Old School Beef Tacos",
         "cook_time" : 30,
         "cats" : "Dinner, Mexican",
         "chef": "amy_hynes",
         },
        {"name": "Easy Chicken Chow Mein",
         "cook_time" : 40,
         "cats" : "Dinner, Chinese",
         "chef": "lynda_faller",
         },
        {"name": "Chicken Curry",
         "cook_time" : 45,
         "cats" : "Dinner, Indian",
         "chef": "eve_ohagan",
         },
        {"name": "California Rolls",
         "cook_time" : 50,
         "cats" : "Lunch, Japanese",
         "chef": "q_smart",
         },]
    cuisines = {"Italian": {"likes": 64 },
            "American": {"likes": 32 },
            "Mexican": {"likes": 16 },
            "Chinese": {"likes": 16 },
            "Indian": {"likes": 16 },
            "Japanese": {"likes": 16 },}

    specials = {"St Patrick's Day": {"likes": 64 },
            "Easter": {"likes": 32 },
            "Christmas": {"likes": 16 },
            "Halloween": {"likes": 16 },
            "4th of July": {"likes": 16 },
            "Valentine's Day": {"likes": 16 },}

    cats = {"Breakfast": {"likes": 64 },
            "Lunch": {"likes": 32 },
            "Dinner": {"likes": 16 },
            "Dessert": {"likes": 16 },
            "Cuisines": {"likes":160},
            "Special Occasions": {"likes": 16 },}

    print(" -Initializing admins . . .")
    for admin, admin_data in admins.items():
        u = add_user(admin,admin_data)
        admin_objects[admin] = u

    print(" -Creating Categories . . .")
    for cat, cat_data in cats.items():
            c = add_cat(cat,cat_data["likes"], 'CAT', None)
            cat_objects[cat] = c

    print(" -Creating Subcategories . . .")
    for cuisine, cuisine_data in cuisines.items():
            c = add_cat(cuisine,cuisine_data["likes"], 'SUB', cat_objects["Cuisines"])
            cat_objects[cuisine] = c

    for spec, spec_data in specials.items():
            c = add_cat(spec,spec_data["likes"], 'SUB', cat_objects["Special Occasions"])
            cat_objects[spec] = c

    print(" -Adding recipes . . .")
    for recipe in recipes:
        add_recipe(recipe["cats"], recipe["name"], recipe["cook_time"], recipe["chef"])

    print(" -Adding reviews . . .")
    for review, review_data in reviews.items():
        r = add_review(review,review_data)

def add_recipe(cats_lst, name, cook_time, chef):
    r = Recipe.objects.get_or_create(chef=admin_objects[chef], name=name)[0]
    r.name = name
    r.cook_time = cook_time
    cats_lst = cats_lst.split(", ")
    print("   ",name,cats_lst)
    for c in cats_lst:
        r.categories.add(cat_objects[c])
    r.save()
    return r

def add_cat(name, likes, type, supercat):
    print("   ",name, type)
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
        add_chef(user)
    return user

def add_chef(user):
    chef = Chef.objects.get_or_create(user=user)[0]
    chef.save()
    return chef

def add_review(title,review_data):
    recipe_chef = review_data["chef"]
    recipe_name = review_data["recipe"]
    author = review_data["author"]
    rating = review_data["rating"]

    recipe = Recipe.objects.get(chef=admin_objects[recipe_chef], name=recipe_name)
    review = Review.objects.get_or_create(recipe=recipe, author=admin_objects[author])[0]
    review.title = title
    review.rating = review_data["rating"]
    review.save()
    return review

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
    print("Population complete.")
