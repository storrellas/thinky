from django.db import models
import uuid
from treebeard.mp_tree import MP_Node

class Node(MP_Node):
    CELL = 'CELL'
    DATALOGGER = 'DATALOGGER'
    NODE = 'NODE'
    TYPE_CHOICES = [
        (CELL, 'CELL'),
        (DATALOGGER, 'DATALOGGER'),
        (NODE, 'NODE')
    ]

    #uuid = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False) 
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)


    node_order_by = ['name']
    def __str__(self):
        return 'Node: {}'.format(self.name)