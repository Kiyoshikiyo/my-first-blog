
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import base64




class Door(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128, blank=True)
    access_to_doors = models.ManyToManyField(Door, blank=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    uid = models.BinaryField(max_length=15, unique=True, editable=False)
    active = models.BooleanField(default=True)
    note = models.CharField(blank=True, max_length=128)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    access_to_doors = models.ManyToManyField(Door)
    groups_member = models.ManyToManyField(Group)

    def __str__(self):
        return base64.b64encode(self.uid).decode('ascii')
         