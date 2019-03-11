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
    title = forms.CharField(widget=forms.TextInput(),max_length=128, label="Title")
    rating = forms.DecimalField(widget=forms.NumberInput(), min_value=0, max_value=5, required=True, label="Rating 1 to 5")
    comment = forms.CharField(widget=forms.Textarea(),label="Any additional comments")

    class Meta:
        model = Review
        exclude = ('recipe','author','date_posted')

class SuggestForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(), label="Leave a suggestion for a new cuisine or occasion!", required=False)

    class Meta:
        model = Suggestion
        fields = ('comment',)

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(), label="First name", required=True)
    last_name = forms.CharField(widget=forms.TextInput(), label="Last name", required=True)
    email = forms.CharField(widget=forms.EmailInput(), label="Email address", required=True)
    comment = forms.CharField(widget=forms.Textarea(), help_text="Leave your comment or question here.", required=True)

    class Meta:
        model = Contact
        fields = ('first_name','last_name','email','comment')

#asls for name of recipe, a photo, and cook time of recipe
class AddRecipeForm(forms.ModelForm):
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
        ("13","St Patrick's Day"),
        ("14","Easter"),
        ("15","Christmas"),
        ("16","Halloween"),
        ("17","4th of July"),
        ("18","Valentine's Day"),
    )
    name = forms.CharField(widget=forms.TextInput(), help_text="Give your recipe a name", required=True)
    photo = forms.ImageField()
    cook_time = forms.IntegerField(min_value=0, initial=0, help_text="in minutes", required=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    categories = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(),choices=CATEGORIES, required=True)

    class Meta:
        model = Recipe
        fields = ('name','photo','cook_time','categories')



"""
top
<!-- <a href="{% url 'trending' %}">Trending</a>
<a href="{% url 'categories' %}">Categories</a>
<a href="{% url 'myaccount' %}">My Account</a>
-->

bottom
<a href="{% url 'faqs' %}">FAQs</a>
"""
