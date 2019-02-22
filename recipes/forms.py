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

#asks for title of rating, actual rating 0-5, and any additional comments
class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Add a title")
    rating = forms.DecimalField(widget=forms.NumberInput(), min_value=0, max_value=5)
    comment = forms.CharField(help_text="Any additional comments")

    class Meta:
        model = Review
        exclude = ('recipe','author','date_posted')

#asls for name of recipe, a photo, and cook time of recipe
class RecipeForm(forms.ModelForm):
    name = forms.CharField(help_text="Name of your recipe")
    photo = forms.ImageField()
    cook_time = forms.IntegerField()

    class Meta:
        model = Recipe
        fields = ('name','photo','cook_time')
