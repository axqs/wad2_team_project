from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from recipes.models import *
from recipes.forms import *
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

def index(request):
    #get all recipes, order alphabetically by name
    recipes = Recipe.objects.order_by('name')
    #get all categories -- no order
    cats = Category.objects.all()
    #get all recipes under dinner category
    dinners = Category.objects.get(name="Dinner").recipe_set.all()

    context_dict = {'recipes':recipes, 'cats':cats, 'dinners':dinners}
    response = render(request,'recipes/index.html', context=context_dict)
    return response

def about(request):
    #get users that are chefs -- order alphabetically by username
    chefs = Chef.objects.order_by('user')
    context_dict = {'chefs':chefs}

    response = render(request,'recipes/about.html', context=context_dict)
    return response
