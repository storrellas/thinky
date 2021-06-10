from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<int:pk>/', CategoryDetail.as_view()),
]
