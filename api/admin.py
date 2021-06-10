from django.contrib import admin

# Register your models here.
from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from .models import Node, Attribute, NodeAttribute

@admin.register(Node)
class NodeAdmin(TreeAdmin):
    form = movenodeform_factory(Node)
    

    class NodeAttributeInline(admin.TabularInline):
        model = NodeAttribute
        extra = 0

    inlines = [NodeAttributeInline, ]


# @admin.register(Node)
# class NodeAdmin(TreeAdmin):
#     form = movenodeform_factory(Node)

@admin.register(NodeAttribute)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Attribute)
class AuthorAdmin(admin.ModelAdmin):
    pass
