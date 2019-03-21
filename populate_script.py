import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wad2_team_project.settings')
import django
django.setup()
from recipes.models import *
from django.contrib.auth.models import User

cat_objects = {}
admin_objects = {}
bio = "Hello! I enjoy making food the opportunity to upload recipes, share tips, and explore recipes on this website!"
def populate():
	reviews = {"Best pancakes" : {"author" : "q_smart", "recipe" : "Pancakes", "chef" : "lynda_faller", "rating" : 4.25, "comment":"These pancakes are so light and fulffy!"}
	}
	admins = {
		"lynda_faller" : {"email":"lynda@gmail.com", "password":"lyndafaller", "fname":"Lynda", "lname":"Faller", "chef":True, "photo":"profile_pics/lynda.png",},
		"amy_hynes" : {"email":"amy@gmail.com", "password":"amyhynes", "fname":"Amy", "lname":"Hynes", "chef":True, "photo":"profile_pics/amy.png",},
		"eve_ohagan" : {"email":"eve@gmail.com", "password":"eveohagan", "fname":"Eve", "lname":"O'Hagan", "chef":True, "photo":"profile_pics/eve.png",},
		"q_smart" : {"email":"q@gmail.com", "password":"qiufeismart", "fname":"Q", "lname":"Smart", "chef":True, "photo":"profile_pics/q.png",},}
	#EVERY TIME THERE IS A RETURN STATEMENT IN ABOUT/INGREDIENTS/STEPS USE \r\n
	recipes = [
		{"name": "Pancakes",
		"cook_time" : 15,
		"cats" : "Breakfast, American",
		"chef" : "lynda_faller",
		"photo" : "pancakes.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "Chicken Pesto Panini",
		"cook_time" : 10,
		"cats" : "Lunch, American",
		"chef" : "eve_ohagan",
		"photo" : "panini.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "All-American Burger",
		"cook_time" : 25,
		"cats" : "Dinner, American, 4th of July",
		"chef" : "q_smart",
		"photo" : "burger.png",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "Traditional Tiramisu",
		"cook_time" : 30,
		"cats" : "Dessert, Italian",
		"chef" : "amy_hynes",
		"photo" : "tirimisu.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "Shamrock Shake",
		"cook_time" : 35,
		"cats" : "Dessert, St Patrick's Day",
		"chef" : "eve_ohagan",
		"photo" : "shake.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "Spaaghetti Carbonara",
		"cook_time" : 35,
		"cats" : "Dinner, Italian",
		"chef" : "amy_hynes",
		"photo" : "carbonara.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "Classic Hot Dogs",
		"cook_time" : 30,
		"cats" : "Lunch, American, 4th of July",
		"chef" : "lynda_faller",
		"photo" : "hotdog.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "Old School Beef Tacos",
		"cook_time" : 30,
		"cats" : "Dinner, Mexican",
		"chef" : "amy_hynes",
		"photo" : "tacos.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "Easy Chicken Chow Mein",
		"cook_time" : 40,
		"cats" : "Dinner, Chinese",
		"chef" : "lynda_faller",
		"photo" : "chowmein.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "Chicken Curry",
		"cook_time" : 45,
		"cats" : "Dinner, Indian",
		"chef" : "eve_ohagan",
		"photo" : "curry.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "St Paddy's Cupcakes",
		"cook_time" : 25,
		"cats" : "Dessert, St Patrick's Day",
		"chef" : "q_smart",
		"photo" : "cupcakes.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},
		{"name": "California Rolls",
		"cook_time" : 50,
		"cats" : "Lunch, Japanese",
		"chef" : "q_smart",
		"photo" : "sushi.jpeg",
		"about": "",
		"ingredients":"",
		"steps":"",
		},]
	cuisines = {"Italian": {"likes": 64, "photo":"italian.jpeg"},
		"American": {"likes": 32, "photo":"american.jpeg"},
		"Mexican": {"likes": 16, "photo":"mexican.jpeg"},
		"Chinese": {"likes": 16, "photo":"chinese.jpeg"},
		"Indian": {"likes": 16, "photo":"indian.jpeg"},
		"Japanese": {"likes": 16, "photo":"japanese.png"},}

	specials = {"St Patrick's Day": {"likes": 64, "photo":"stpaddys.jpeg"},
		"Easter": {"likes": 32, "photo":"easter.jpeg"},
		"Christmas": {"likes": 16, "photo":"christmas.jpeg"},
		"Halloween": {"likes": 16, "photo":"halloween.jpeg"},
		"4th of July": {"likes": 16, "photo":"4july.jpeg"},
		"Valentine's Day": {"likes": 16, "photo":"valentines.jpeg"},}

	cats = {"Breakfast": {"likes": 64, "photo":"breakfast.jpeg"},
		"Lunch": {"likes": 32, "photo":"lunch.jpeg"},
		"Dinner": {"likes": 16, "photo":"dinner.jpeg"},
		"Dessert": {"likes": 16, "photo":"dessert.jpeg"},
		"Cuisines": {"likes":160, "photo":"cuisines.jpeg"},
		"Special Occasions": {"likes": 160, "photo":"spec_occ.jpeg"},}

	print(" -Initializing admins . . .")
	for admin, admin_data in admins.items():
		u = add_user(admin,admin_data)
		admin_objects[admin] = u

	print(" -Creating Categories . . .")
	for cat, cat_data in cats.items():
		c = add_cat(cat,cat_data["likes"], 'CAT', None, cat_data["photo"])
		cat_objects[cat] = c

	print(" -Creating Subcategories . . .")
	for cuisine, cuisine_data in cuisines.items():
		c = add_cat(cuisine,cuisine_data["likes"], 'CUS', cat_objects["Cuisines"], cuisine_data["photo"])
		cat_objects[cuisine] = c

	for spec, spec_data in specials.items():
		c = add_cat(spec,spec_data["likes"], 'SPE', cat_objects["Special Occasions"], spec_data["photo"])
		cat_objects[spec] = c

	print(" -Adding recipes . . .")
	for recipe in recipes:
		add_recipe(recipe["cats"], recipe["name"], recipe["cook_time"], recipe["chef"], recipe["photo"])

	print(" -Adding reviews . . .")
	for review, review_data in reviews.items():
		r = add_review(review,review_data)

def add_recipe(cats_lst, name, cook_time, chef, photo):
	r = Recipe.objects.get_or_create(chef=admin_objects[chef], name=name)[0]
	r.name = name
	r.cook_time = cook_time
	cats_lst = cats_lst.split(", ")
	print("   ",name,cats_lst)
	for c in cats_lst:
		r.categories.add(cat_objects[c])
	r.photo = "food_pics/"+photo
	r.save()
	return r

def add_cat(name, likes, type, supercat, photo):
	print("   ",name, type)
	if type == 'CUS' or type == 'SPE':
		c = Category.objects.get_or_create(name=name, type=type, supercat=supercat)[0]
	else:
		c = Category.objects.get_or_create(name=name, type=type)[0]
	c.likes=likes
	c.photo = "cat_pics/"+photo
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
		add_chef(user,user_data)
	return user

def add_chef(user,user_data):
	chef = Chef.objects.get_or_create(user=user)[0]
	chef.photo = user_data["photo"]
	chef.bio = bio
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
