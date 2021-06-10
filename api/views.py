from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

from django.contrib.auth.models import User

from .models import Category

from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategoryList(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get(self, request, format=None):
      """
      Return a list of all categories.
      """
      root = Category.objects.get(depth=1)
      return Response({'tree': Category.dump_bulk()[0]})

    def post(self, request):

      parent = Category.objects.get(id=request.data['parent_id'])
      category = Category(name=request.data['data']['name'])
      parent.add_child(instance=category)
      serializer = CategorySerializer(category)
      return Response({'message': serializer.data})

class CategoryDetail(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    def get(self, request, pk, format=None):
      """
      Return a list of all categories.
      """
      item = Category.objects.get(id=pk)
      return Response({'tree': Category.dump_bulk(item)[0]})

    def delete(self, request, pk, format=None):
      """
      Return a list of all categories.
      """
      Category.objects.get(id=pk).delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 
