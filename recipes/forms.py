from django import forms
from recipes.models import *
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password','first_name','last_name')

# our version of UserProfile
class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = ('photo',)

#asks for title of rating, actual rating 0-5 decimal, and any additional comments
class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Add a title")
    rating = forms.DecimalField(widget=forms.NumberInput(), min_value=0, max_value=5)
    comment = forms.CharField(help_text="Any additional comments")

    class Meta:
        model = Review
        exclude = ('recipe','author','date_posted')

class SuggestForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(), help_text="Leave a suggestion for a new cuisine or occasion!", required=False)

    class Meta:
        model = Suggestion
        fields = ('comment',)

#asls for name of recipe, a photo, and cook time of recipe
class RecipeForm(forms.ModelForm):
    CATEGORIES =(
        ("1","Breakfast"),
        ("2","Lunch"),
        ("3","Dinner"),
        ("4","Dessert"),
        ("6","Italian"),
        ("7","American"),
        ("8","Mexican"),
        ("9","Chinese"),
        ("10","Indian"),
        ("11","Japanese"),
        ("12","Special Occasions"),
    )
    name = forms.CharField(widget=forms.TextInput(), help_text="Name of your recipe")
    photo = forms.ImageField()
    cook_time = forms.IntegerField(min_value=0, initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=CATEGORIES)

#for view
#if form.is_valid():
#            cats = form.cleaned_data.get('categories')
#views part get username
#def my_view(request):
#    username = None
#    if request.user.is_authenticated():
#        username = request.user.username
#for templates i think
#<form method='post'>
#    {{ form.as_p }}
#    <input type='submit' value='submit'>
#</form>

    class Meta:
        model = Recipe
        fields = ('name','photo','cook_time','categories')



"""
top
<!-- <a href="{% url 'trending' %}">Trending</a>
<a href="{% url 'categories' %}">Categories</a>
<a href="{% url 'login' %}">Login/a>
-->

bottom
<!-- <a href="{% url 'contact' %}">Contact Us</a>
<a href="{% url 'faqs' %}">FAQs</a>
<a href="{% url 'suggest' %}">Suggest Cuisine</a> -->
"""
