from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    TYPES = (
        ('CAT', 'Category'),
        ('SUB', 'Subcategory')
    )
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=25, choices=TYPES)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    supercat = models.ForeignKey('self', null=True, related_name='category')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Chef(models.Model):
    user = models.OneToOneField(User)
    username =  models.CharField(max_length=128)
    fname =  models.CharField(max_length=128)
    lname =  models.CharField(max_length=128)
    email = models.EmailField()
    photo = models.ImageField(upload_to='profile_pics', default='profile_pics/anon.png')

    def __str__(self):
        return self.user.username

class Recipe(models.Model):
    chef = models.ForeignKey(User)
    slug = models.SlugField(unique=True)
    categories = models.ManyToManyField(Category)
    name = models.CharField(max_length=128, unique=True)
    photo = models.ImageField(upload_to='food_pics', blank=True)
    cook_time = models.IntegerField(default=0)
    #ingredients, steps, overall rating

    def save(self, *args, **kwargs):
        self.slug = slugify(self.chef.username+"-"+self.name)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Review(models.Model):
    recipe = models.ForeignKey(Recipe)
    author = models.ForeignKey(Chef)
    title = models.CharField(max_length=50, default="My Rating")
    rating = models.DecimalField(decimal_places=2,max_digits=3,default=5.00)
