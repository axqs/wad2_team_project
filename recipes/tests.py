from django.test import TestCase

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.contrib import admin
from selenium import webdriver
from django.core.urlresolvers import reverse
import os
import socket

# Create your tests here.

#so this is to be run in the way described in the book, not the complicated way with rango_tests folder!
#take tests from rango_tests folder for ideas but for actual tests u want one file
#The django mini book tests are as below
#Make tests based on not chapter but on page view, so sort these out based on
#the view they belong to

#------------------------------------------------------------------------------------------------
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders
from recipes.models import Chef, Category, Recipe, Review, Suggestion
import populate_recipes
import recipes.test_utils as test_utils

class NeighbourhoodCookbookGeneralTests(TestCase):

    #1: might not be running this?
    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds logo.png
        result = finders.find('images/logo.png')
        self.assertIsNotNone(result)

class NeighbourhoodCookbookIndexPageTests(TestCase):
    def setUp(self):
        try:
            from populate_recipes import populate
            populate()
        except ImportError:
            print('The module populate_recipes does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')


    def get_category(self, name):

        from recipes.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat
    #2
    def test_index_contains_popularcuisines(self):
        # Check if there is a welcome message
        print(TestCase)
        response = self.client.get(reverse('index'))
        self.assertIn(b'Popular Cuisines', response.content)
    #3
    def test_index_contains_latestposts(self):
        # Check if there is a welcome message
        print(TestCase)
        response = self.client.get(reverse('index'))
        self.assertIn(b'Latest Posts', response.content)
    #4
    def test_index_contains_toprated(self):
        # Check if there is a welcome message
        print(TestCase)
        response = self.client.get(reverse('index'))
        self.assertIn(b'Top Rated Recipes', response.content)
                      
    #5
    def test_index_using_template(self):
        # Check the template used to render index page
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'recipes/index.html')
    #6
    def test_does_index_contain_img(self):
        # Check if the index page contains an img
        response = self.client.get(reverse('index'))
        self.assertIn(b'img', response.content)
    #7
    def test_logo_picture_displayed(self):
        # Check if is there an image called 'logo.png' on the index page
        response = self.client.get(reverse('index'))
        self.assertIn(b'img src="/static/images/logo.png', response.content)
    #8
    def test_index_has_title(self):
        # Check to make sure that the title tag has been used
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class NeighbourhoodCookbookAboutPageTests(TestCase):
##    def setUp(self):
##        try:
##            from populate_recipes import populate
##            populate()
##        except ImportError:
##            print('The module populate_recipes does not exist')
##        except NameError:
##            print('The function populate() does not exist or is not correct')
##        except:
##            print('Something went wrong in the populate() function :-(')
##
    def get_category(self, name):

        from recipes.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat
    #9
    def test_about_contains_about_message(self):
        # Check if in the about page is there - and contains the specified message
        response = self.client.get(reverse('about'))
        self.assertIn(b'About', response.content)
        #do we need the b?^
    #10
    def test_about_contain_any_img(self):
        # Check if in the about page contains an image
        response = self.client.get(reverse('about'))
        self.assertIn(b'img', response.content)

    #11
    def test_about_contain_profile_image(self):
        # Check if is there an image of at least one of us on the about page
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/media/profile_pics', response.content)

    #12
    def test_about_using_template(self):
        # Check the template used to render index page
        # Exercise from Chapter 4
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'recipes/about.html')

class NeighbourhoodCookbookModelTests(TestCase):

    def setUp(self):
        try:
            from populate_recipes import populate
            populate()
        except ImportError:
            print('The module populate_recipes does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')


    def get_category(self, name):

        from recipes.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    #13
    def test_cuisines_cat_added(self):
        cat = self.get_category('Cuisines')
        self.assertIsNotNone(cat)

    #14
    def test_special_occasions_cat_added(self):
        cat = self.get_category('Special Occasions')
        self.assertIsNotNone(cat)
    #15
    def test_dessert_cat_added(self):
        cat = self.get_category('Dessert')
        self.assertIsNotNone(cat)

    #16
    def test_breakfast_cat_added(self):
        cat = self.get_category('Breakfast')
        self.assertIsNotNone(cat)
    #17
    def test_lunch_cat_added(self):
        cat = self.get_category('Lunch')
        self.assertIsNotNone(cat)
    #18
    def test_dinner_cat_added(self):
        cat = self.get_category('Dinner')
        self.assertIsNotNone(cat)
    #19
    def test_cuisines_cat_with_likes(self):
        cat = self.get_category('Cuisines')
        self.assertEqual(cat.likes, 160)

    #20
    def test_special_occasions_cat_with_likes(self):
        cat = self.get_category('Special Occasions')
        self.assertEqual(cat.likes, 160)
    #21
    def test_dessert_cat_with_likes(self):
        cat = self.get_category('Dessert')
        self.assertEqual(cat.likes, 16)
    #22
    def test_breakfast_cat_with_likes(self):
        cat = self.get_category('Breakfast')
        self.assertEqual(cat.likes, 64)
    #23
    def test_lunch_cat_with_likes(self):
        cat = self.get_category('Lunch')
        self.assertEqual(cat.likes, 32)
    #24
    def test_dinner_cat_with_likes(self):
        cat = self.get_category('Dinner')
        self.assertEqual(cat.likes, 16)

class NeighbourhoodOtherViewTests(TestCase):

    def setUp(self):
        try:
            from populate_recipes import populate
            populate()
        except ImportError:
            print('The module populate_recipes does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_category(self, name):

        from recipes.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    # Need to add tests to:
    # check admin interface - is it configured and set up
    #25
    def test_admin_interface_recipe_view(self):
        from recipes.admin import RecipeAdmin
        self.assertIn('name', RecipeAdmin.list_display)
        self.assertIn('cook_time', RecipeAdmin.list_display)
        self.assertIn('chef', RecipeAdmin.list_display)

    #26
    # check admin interface: Category
    def test_admin_interface_category_view(self):
        from recipes.admin import CategoryAdmin
        self.assertIn('slug', CategoryAdmin.prepopulated_fields)
 #       self.assertIn('type', CategoryAdmin.prepopulated_fields)

    #27
    # check admin interface: Review
    def test_admin_interface_review_view(self):
        from recipes.admin import ReviewAdmin
        self.assertIn('recipe', ReviewAdmin.list_display)
        self.assertIn('author', ReviewAdmin.list_display)
        self.assertIn('rating', ReviewAdmin.list_display)
        self.assertIn('comment', ReviewAdmin.list_display)

    #28
    # check admin interface
    def test_admin_interface_suggestion_view(self):
        from recipes.admin import SuggestionAdmin
        self.assertIn('comment', SuggestionAdmin.list_display)
        self.assertIn('author', SuggestionAdmin.list_display)

    #29
    # test the slug field works..
    def test_does_slug_field_work(self):
        from recipes.models import Category
        cat = Category(name='how do i create a slug in django')
        cat.save()
        self.assertEqual(cat.slug,'how-do-i-create-a-slug-in-django')

    #30
    # are categories displayed on index page?
    def category_displayed_in_index(self):
        cat = self.get_category('Cuisines')
        if (self.assertIsNotNone(cat)):
            # Check if in the categories page contains a category
            response = self.client.get(reverse('categories'))
            self.assertIn(cat, response.content)


class Chapter5ModelTests(TestCase):

    def setUp(self):
        try:
            from populate_recipes import populate
            populate()
        except ImportError:
            print('The module populate_recipes does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_category(self, name):

        from recipes.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat
    #42
    def test_create_a_new_category(self):
        categories_in_database = Category.objects.all()
        self.assertEquals(len(categories_in_database), 18)
        from populate_recipes import add_cat
        cat = Category(name="create_a_new_category_test")
        cat.save()
        categories_in_database = Category.objects.all()
        # Check category is in database. 18 categories exist already, so we want
        #to make sure that there is now 19
        self.assertEquals(len(categories_in_database), 19)
        #category gets appended onto last
        last_poll_in_database = categories_in_database[18]
        self.assertEquals(last_poll_in_database, cat)
    #43
    def test_create_recipes_for_categories(self):
        from populate_recipes import add_user, add_cat, add_recipe
        #check that categories is 18 to start with
        categories_in_database = Category.objects.all()
        self.assertEquals(len(categories_in_database), 18)
        #add the vegan category
        cat = Category(name="Vegan")
        cat.save()
        # Check Vegan is in database. 19 categories should exist now
        categories_in_database = Category.objects.all()
        self.assertEquals(len(categories_in_database), 19)

        chef=add_user("new_user", {"email":"newuser@gmail.com", "password":"newuser", "fname":"New", "lname":"User", "chef":True, "photo":"anon.png",})
        # create 2 pages for category python
        #it makes the foreign key within the method so we need to use the method
        vegan_recipe=add_recipe(cat, "Best Double Chcolate Chip Brownies", 50, chef, "veganrecipe.jpeg") 
 #       vegan_recipe = Recipe()
        #vegan_recipe.name="Best Double Chocolate Chip Brownies"
        #vegan_recipe.chef=add_user("new_user", {"email":"newuser@gmail.com", "password":"newuser", "fname":"New", "lname":"User", "chef":True, "photo":"anon.png",})
        #recipe needs to have id, and that's cats_lst, but it also needs catgories field
        #vegan_recipe.r = Recipe.objects.get_or_create(chef=vegan_recipe.chef, name=vegan_recipe.name)[0]
 #       vegan_recipe.cats_lst = cat
 #       vegan_recipe.cats = cat
 #       vegan_recipe.categories = cat
 #       vegan_recipe.cook_time= 50
#        vegan_recipe.save()
        chef2=add_user("new_user", {"email":"newuser2@gmail.com", "password":"newuser2", "fname":"New", "lname":"User2", "chef":True, "photo":"anon.png",})
        vegan_recipe=add_recipe(cat, "Vanilla Funfetti Cake", 70, chef2, "veganrecipe2.jpeg") 

 #       vegan_recipe2 = Recipe()
 #       vegan_recipe2.chef=add_user("new_user2", {"email":"newuser2@gmail.com", "password":"newuser2", "fname":"New", "lname":"User2", "chef":True, "photo":"anon.png",})
#
 #       vegan_recipe2.cats_lst = cat
 #       vegan_recipe2.categories = cat
 #       vegan_recipe.cats = cat
        
 #       vegan_recipe2.name="Vanilla Funfetti Cake"
 #       vegan_recipe2.cook_time= 70
 #       vegan_recipe2.save()
 #       cat.save()

        # Check if they both were saved
        vegan_test_recipes = cat.recipe_set.all()
        #FOR SOME REASON STILL DOESNT WORK CUZ OF FOREIGN KEY!
        self.assertEquals(vegan_test_recipes.count(), 2)

        #Check if they were saved properly
        first_recipe = vegan_test_recipes[0]
        self.assertEquals(first_recipe, vegan_recipe)
        self.assertEquals(first_recipe.chef , new_user)
        self.assertEquals(first_recipe.name, "Best Double Chocolate Chip Brownies")
        self.assertEquals(first_recipe.cook_time, 50)
    #44
    def test_population_script_changes(self):
        #Populate database
        populate_recipes.populate()

        # Check if the category has correct number of likes
        cat = Category.objects.get(name='Special Occasions')
        self.assertEquals(cat.likes, 160)

        # Check if the category has correct number of likes
        cat = Category.objects.get(name='Breakfast')
        self.assertEquals(cat.likes, 64)

        # Check if the category has correct number of likes
        cat = Category.objects.get(name='Lunch')
        self.assertEquals(cat.likes, 32)

        # Check if the category has correct number of likes
        cat = Category.objects.get(name='Dinner')
        self.assertEquals(cat.likes, 16)

        # Check if the category has correct number of likes
        cat = Category.objects.get(name='Dessert')
        self.assertEquals(cat.likes, 16)

        # Check if the category has correct number of likes
        cat = Category.objects.get(name='Cuisines')
        self.assertEquals(cat.likes, 160)
