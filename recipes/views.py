from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import recipes.models
import recipes.forms
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
# Create your views here.

def index(request):
    return HttpResponse("Hello")
