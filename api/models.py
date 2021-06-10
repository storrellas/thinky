from django.db import models
import uuid
from treebeard.mp_tree import MP_Node
from django.utils import timezone


CELL = 'CELL'
DATALOGGER = 'DATALOGGER'
NODE = 'NODE'
TYPE_CHOICES = [
    (CELL, 'CELL'),
    (DATALOGGER, 'DATALOGGER'),
    (NODE, 'NODE')
]

class Attribute(models.Model):
    HMI = 'HMI'
    WWI = 'WWI'
    STR = 'STR'
    XLS = 'XLS'
    CATEGORY_CHOICES = [
        (HMI, 'HMI'),
        (WWI, 'WWI'),
        (STR, 'STR'),
        (XLS, 'XLS')
    ]
    uuid = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False) 
    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(
        max_length=3, choices=CATEGORY_CHOICES, null=True, blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)


class Node(MP_Node):
    uuid = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False) 
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)

    node_order_by = ['name']
    def __str__(self):
        return 'Node: {}'.format(self.name)

class NodeAttribute(models.Model):
    GOOD = 'GOOD'
    BAD = 'BAD'
    UNKNOWN = 'UNKNOWN'
    SUSPECT = 'SUSPECT'
    QUALITY_CHOICES = [
        (GOOD, 'GOOD'),
        (BAD, 'BAD'),
        (UNKNOWN, 'UNKNOWN'),
        (SUSPECT, 'SUSPECT')
    ]
    uuid = models.UUIDField( primary_key = True, default = uuid.uuid4, editable = False) 
    svalue = models.CharField(max_length=255, null=True, blank=True)
    fvalue = models.FloatField(null=True, blank=True)
    dupdate = models.DateTimeField(null=True, blank=True, default=timezone.now)
    quality = models.CharField(
        max_length=7, choices=QUALITY_CHOICES, null=True, blank=True, default='unknown')
    attributes = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='node_attributes', null=True, blank=True)
    nodes = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='node_attributes', null=True, blank=True)
