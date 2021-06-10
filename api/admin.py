from django.contrib import admin

# Register your models here.
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Category

class CategoryAdmin(TreeAdmin):
    form = movenodeform_factory(Category)

admin.site.register(Category, CategoryAdmin)