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
    def test_index_contains_recipes(self):
        # Check if there is a welcome message
        print(TestCase)
        response = self.client.get(reverse('index'))
        self.assertIn(b'Recipes', response.content)
    #3
    def test_index_contains_categories(self):
        # Check if there is a welcome message
        print(TestCase)
        response = self.client.get(reverse('index'))
        self.assertIn(b'Categories', response.content)
    #4
    def test_index_contains_reviews(self):
        # Check if there is a welcome message
        print(TestCase)
        response = self.client.get(reverse('index'))
        self.assertIn(b'Reviews', response.content)
                      
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
        self.assertEqual(cat.likes, 16)
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


class NCChapter6ViewTests(TestCase):

    def setUp(self):
        try:
            from populate_rango import populate
            populate()
        except ImportError:
            print('The module populate_rango does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')


    # are categories displayed on index page?

    # does the category model have a slug field?


    # test category view does the page exist?


    # test whether you can navigate from index to a category page


    # test does index page contain top five pages?

    # test does index page contain the words "most liked" and "most viewed"

    # test does category page contain a link back to index page?



class NCChapter7ViewTests(TestCase):

    def setUp(self):
        try:
            from forms import PageForm
            from forms import CategoryForm

        except ImportError:
            print('The module forms does not exist')
        except NameError:
            print('The class PageForm does not exist or is not correct')
        except:
            print('Something else went wrong :-(')

    pass
    # test is there a PageForm in rango.forms

    # test is there a CategoryForm in rango.forms

    # test is there an add page page?

    # test is there an category page?


    # test if index contains link to add category page
    #<a href="/rango/add_category/">Add a New Category</a><br />


    # test if the add_page.html template exists.

#--------------------------------------------------------------------------------
#original ch 3 tests
class NeighborhoodCookbookLiveServerTests(StaticLiveServerTestCase):
    def setUp(self):
 #       driver = webdriver.Chrome('/chromedriver')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options = chrome_options)
        self.browser.implicitly_wait(3)

    @classmethod
    def setUpClass(cls):
        cls.host = socket.gethostbyname(socket.gethostname())
        super(NeighborhoodCookbookLiveServerTests, cls).setUpClass()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()


 #ALL the navigation testing
    #31
    def test_navigate_from_index_to_about(self):
        # Go to recipes main page
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        print(url)
        self.browser.get(url + reverse('index'))

        # Search for a link to About page
        about_link = self.browser.find_element_by_partial_link_text("About")
        about_link.click()

        # Check if it goes back to the home page
        self.assertIn(url + reverse('about'), self.browser.current_url)
    #32
    def test_navigate_from_about_to_index(self):
        # Go to recipes main page
        self.client.get(reverse('index'))
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('about'))

        # Check if there is a link back to the home page
        # link_to_home_page = self.browser.find_element_by_tag_name('a')
        link_to_home_page = self.browser.find_element_by_link_text('Index')
        link_to_home_page.click()

        # Check if it goes back to the home page
        self.assertEqual(url + reverse('index'), self.browser.current_url)
#----------------------------------------------------------------------------
    #33
    def test_navigate_from_index_to_contactus(self):
        # Go to recipes main page
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        print(url)
        self.browser.get(url + reverse('index'))

        # Search for a link to contactus page
        contact_us_link = self.browser.find_element_by_partial_link_text("Contact")
        contact_us_link.click()
        #Check if it goes back to the home page
        self.assertIn(url + reverse('contactus'), self.browser.current_url)

    #34
    def test_navigate_from_contactus_to_index(self):
        # Go to recipes main page
        self.client.get(reverse('index'))
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('contactus'))

        # Check if there is a link back to the home page
        # link_to_home_page = self.browser.find_element_by_tag_name('a')
        link_to_home_page = self.browser.find_element_by_link_text('Index')
        link_to_home_page.click()

        # Check if it goes back to the home page
        self.assertEqual(url + reverse('index'), self.browser.current_url)
#----------------------------------------------------------------------------
    #35
    def test_navigate_from_index_to_faqs(self):
        # Go to recipes main page
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        print(url)
        self.browser.get(url + reverse('index'))

        # Search for a link to faqs page
        faqs_link = self.browser.find_element_by_partial_link_text("FAQs")
        faqs_link.click()
        #Check if it goes back to the home page
        self.assertIn(url + reverse('faqs'), self.browser.current_url)

    #36
    def test_navigate_from_faqs_to_index(self):
        # Go to recipes main page
        self.client.get(reverse('index'))
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('faqs'))

        # Check if there is a link back to the home page
        # link_to_home_page = self.browser.find_element_by_tag_name('a')
        link_to_home_page = self.browser.find_element_by_link_text('Index')
        link_to_home_page.click()

        # Check if it goes back to the home page
        self.assertEqual(url + reverse('index'), self.browser.current_url)
#----------------------------------------------------------------------------
    #37
    def test_navigate_from_index_to_suggestcuisine(self):
        # Go to recipes main page
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        print(url)
        self.browser.get(url + reverse('index'))

        # Search for a link to contactus page
        suggest_cuisine_link = self.browser.find_element_by_partial_link_text("SuggestCuisine")
        suggest_cuisine_link.click()
        #Check if it goes back to the home page
        self.assertIn(url + reverse('suggestion'), self.browser.current_url)

    #38
    def test_navigate_from_suggestcuisine_to_index(self):
        # Go to recipes main page
        self.client.get(reverse('index'))
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('suggestion'))

        # Check if there is a link back to the home page
        # link_to_home_page = self.browser.find_element_by_tag_name('a')
        link_to_home_page = self.browser.find_element_by_link_text('Index')
        link_to_home_page.click()

        # Check if it goes back to the home page
        self.assertEqual(url + reverse('index'), self.browser.current_url)


#--------------------------------------------------------------------------------------------------------------------
#look at models.py to create test for the subcategories
        #git pull first though
class NeighbourhoodCookbookLiveServerTests2(StaticLiveServerTestCase):

    def setUp(self):
        from django.contrib.auth.models import User
        User.objects.create_superuser(username='admin', password='admin', email='admin@me.com')
        #chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("test-type")
        #self.browser = webdriver.Chrome(chrome_options=chrome_options)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        self.browser = webdriver.Chrome(chrome_options = chrome_options)
        self.browser.implicitly_wait(3)

    @classmethod
    def setUpClass(cls):
        cls.host = socket.gethostbyname(socket.gethostname())
        super(NeighbourhoodCookbookLiveServerTests2, cls).setUpClass()

    def tearDown(self):
        self.browser.refresh()
        self.browser.quit()
    #39
    def test_population_script(self):
        #Populate database
        populate_recipes.populate()
        url = self.live_server_url
        #url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('admin:index'))

        # Log in the admin page
        test_utils.login(self)

        # # Check if is there link to categories
        # category_link = self.browser.find_elements_by_partial_link_text('Categor')
        # print(category_link[0].text)
        # category_link[0].click()

        # Check for the categories saved by the population script
        # self.browser.find_elements_by_partial_link_text('Other Frameworks')
        # self.browser.find_elements_by_partial_link_text('Django')
        # self.browser.find_elements_by_partial_link_text('Python')

        # Check the recipes saved by the population script
        self.browser.get(url + reverse('admin:rango_page_changelist'))
        self.browser.find_elements_by_partial_link_text('Pancakes')
        self.browser.find_elements_by_partial_link_text('Chicken Pesto Panini')
        self.browser.find_elements_by_partial_link_text('All-American Burger')
        self.browser.find_elements_by_partial_link_text('Traditional Tiramisu')
        self.browser.find_elements_by_partial_link_text("St Paddy's Shake")
        self.browser.find_elements_by_partial_link_text('Spaghetti Carbonara')
        self.browser.find_elements_by_partial_link_text('Classic Hot Dogs')
        self.browser.find_elements_by_partial_link_text('Old School Beef Tacos')
        self.browser.find_elements_by_partial_link_text('Easy Chicken Chow Mein')
        self.browser.find_elements_by_partial_link_text('Chicken Curry')
        self.browser.find_elements_by_partial_link_text('California Rolls')
    #40
    def test_admin_page_contains_name_cooktime_and_chef(self):
        #Populate database
        populate_recipes.populate()

        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('admin:index'))

        # Log in the admin page
        test_utils.login(self)

        # Click in Pages
        recipes_link = self.browser.find_element_by_link_text('Recipes')
        pages_link.click()

        body = self.browser.find_element_by_tag_name('body')

        # Get all pages
        recipes = Recipe.objects.all()

        # Check all recipes name, cook_time and chef are displayed
        for recipe in recipes:
            self.assertIn(recipe.name, body.text)
            #self.assertIn(page.category.name, body.text)
            self.assertIn(recipe.cook_time, body.text)
            self.assertIn(recipe.chef, body.text)


#chnage the links to be links of actual recipes pages
        # Check for the Github account and PythonAnywhere account
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('http://www.djangorocks.com/', body.text)
        self.assertIn('http://flask.pocoo.org', body.text)
    #41
    def test_can_create_new_category_via_admin_site(self):
        #Access admin page
        url = self.live_server_url
        url = url.replace('localhost', '127.0.0.1')
        self.browser.get(url + reverse('admin:index'))

        # Check if it display admin message
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Django administration', body.text)

        # Log in the admin page
        test_utils.login(self)

        # the Site Administration page
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Site administration', body.text)

        # Check if is there link to categories
        category_link = self.browser.find_elements_by_partial_link_text('Categor')
        self.assertEquals(len(category_link), 1)

        # Click in the link
        category_link[0].click()

        # Empty, so check for the empty message
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('0 categor', body.text.lower())

        # Add a category by clicking on 'Add category
        # new_poll_link = self.browser.find_element_by_link_text('Add category')
        new_poll_link = self.browser.find_element_by_class_name('addlink')
        new_poll_link.click()

        # Check for input field
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Name:'.lower(), body.text.lower())

        # Input category name
        category_field = self.browser.find_element_by_name('name')
        category_field.send_keys("Test Driven Development")

        # Leave likes and views as 0

         # Gertrude clicks the save button
        save_button = self.browser.find_element_by_css_selector("input[value='Save']")
        save_button.click()

        # As redirected there is a link for the category
        # category_link1 = self.browser.find_elements_by_link_text("Test Driven Development")

        # self.assertEquals(len(category_link1), 0)


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
        self.assertEquals(cat.likes, 16)

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
