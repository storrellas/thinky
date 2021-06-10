from django.contrib import admin

# Register your models here.
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Node

@admin.register(Node)
class NodeAdmin(TreeAdmin):
    pass

