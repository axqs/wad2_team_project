from django.contrib import admin
from recipes.models import *

# Register your models here.

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name','cook_time','chef')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name', 'type')}

class ChefAdmin(admin.ModelAdmin):
    list_display = ('username','fname','lname','email')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('recipe','author','rating')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Chef, ChefAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Review, ReviewAdmin)
