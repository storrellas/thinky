from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('node/', NodeList.as_view()),
    path('node/<int:pk>/', NodeDetail.as_view()),
]
