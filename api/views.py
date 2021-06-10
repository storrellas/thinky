from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework import status

from django.contrib.auth.models import User

from .models import Node, NodeAttribute

from rest_framework import serializers


class NodeAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodeAttribute
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):
    node_attributes = NodeAttributeSerializer(many=True)
    class Meta:
        model = Node
        fields = ['name', 'description', 'node_attributes']

class NodeList(APIView):

    def serialize(self, node):
      serializer_node = NodeSerializer(node)
      children = []
      for item in node.get_descendants():
        #serializer_node = NodeSerializer(item)
        children.append( self.serialize(item) )

      return {'node': serializer_node.data, 'children': children}

    def get(self, request, format=None):
      root = Node.objects.get(depth=1)
      # print( "get_children ", root.get_children() )
      # print( "get_descendants ", root.get_descendants() )
      # print( "get_descendants ", self.serialize(root) )
      return Response({'tree': self.serialize(root)})
      #return Response({'tree': Node.dump_bulk()[0]})

    def post(self, request):
      parent = Node.objects.get(id=request.data['parent_id'])
      instance = Node(name=request.data['data']['name'])
      parent.add_child(instance=instance)
      serializer = NodeSerializer(node)
      return Response({'message': serializer.data})

class NodeDetail(APIView):

    def get(self, request, pk, format=None):
      item = Node.objects.get(id=pk)
      return Response({'tree': Node.dump_bulk(item)[0]})

    def delete(self, request, pk, format=None):
      Node.objects.get(id=pk).delete()
      return Response(status=status.HTTP_204_NO_CONTENT) 
