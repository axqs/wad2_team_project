from django.test import TestCase

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
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

# Thanks to Enzo Roiz https://github.com/enzoroiz who made these tests during an internship with us

# The following tests are adapted from the textbook: How to Tango With Django
#TO CREATE YOUR OWN TESTS: READ THESE LINKS
#https://docs.djangoproject.com/en/2.1/topics/testing/overview/
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing


class NeighbourhoodCookbookGeneralTests(TestCase):
    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds logo.png
        result = finders.find('images/logo.png')
        self.assertIsNotNone(result)

class NeighbourhoodCookbookIndexPageTests(TestCase):
        
    def test_index_contains_welcome_message(self):
        # Check if there is a welcome message 
        response = self.client.get(reverse('index'))
        self.assertIn(b'Welcome', response.content)
         
    def test_index_using_template(self):
        # Check the template used to render index page
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'recipes/index.html')

    def test_does_index_contain_img(self):
        # Check if the index page contains an img
        response = self.client.get(reverse('index'))
        self.assertIn('img', response.content)

    def test_logo_picture_displayed(self):
        # Check if is there an image called 'logo.png' on the index page
        response = self.client.get(reverse('index'))
        self.assertIn(b'img src="/static/images/logo.png', response.content)
    
    def test_index_has_title(self):
        # Check to make sure that the title tag has been used
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class NeighbourhoodCookbookAboutPageTests(TestCase):
        
    def test_about_contains_about_message(self):
        # Check if in the about page is there - and contains the specified message
        response = self.client.get(reverse('about'))
        self.assertIn(b'About Us', response.content)
        #do we need the b?^

    def test_about_contain_any_img(self):
        # Check if in the about page contains an image
        response = self.client.get(reverse('about'))
        self.assertIn('img', response.content)
               
    def test_about_contain_image(self):
        # Check if is there an image of at least one of us on the about page
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/media/profile_pics', response.content)

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
        
    def test_cuisines_cat_added(self):
        cat = self.get_category('Cuisines')  
        self.assertIsNotNone(cat)
        
    def test_special_occasions_cat_added(self):
        cat = self.get_category('Special Occasions')  
        self.assertIsNotNone(cat)
        
    def test_dessert_cat_added(self):
        cat = self.get_category('Dessert')  
        self.assertIsNotNone(cat)

    def test_breakfast_cat_added(self):
        cat = self.get_category('Breakfast')  
        self.assertIsNotNone(cat)

    def test_lunch_cat_added(self):
        cat = self.get_category('Lunch')  
        self.assertIsNotNone(cat)

    def test_dinner_cat_added(self):
        cat = self.get_category('Dinner')  
        self.assertIsNotNone(cat)
         
    def test_cuisines_cat_with_likes(self):
        cat = self.get_category('Cuisines')
        self.assertEqual(cat.likes, 0)
        
    def test_special_occasions_cat_with_likes(self):
        cat = self.get_category('Special Occasions')
        self.assertEqual(cat.likes, 16)
        
    def test_dessert_cat_with_likes(self):
        cat = self.get_category('Dessert')
        self.assertEqual(cat.likes, 16)
        
    def test_breakfast_cat_with_likes(self):
        cat = self.get_category('Breakfast')
        self.assertEqual(cat.likes, 64)
        
    def test_lunch_cat_with_likes(self):
        cat = self.get_category('Lunch')
        self.assertEqual(cat.likes, 32)
        
    def test_dinner_cat_with_likes(self):
        cat = self.get_category('Dinner')
        self.assertEqual(cat.likes, 16)
        
#class NeighbourhoodCookbookViewTests(TestCase): 

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

        from rango.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    # Need to add tests to:
    # check admin interface - is it configured and set up
    def test_admin_interface_page_view(self):
        from admin import PageAdmin
        self.assertIn('category', PageAdmin.list_display)
        self.assertIn('url', PageAdmin.list_display)
    
    # test the slug field works..
    def test_does_slug_field_work(self):
        from recipes.models import Category
        cat = Category(name='how do i create a slug in django')
        cat.save()
        self.assertEqual(cat.slug,'how-do-i-create-a-slug-in-django')

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
