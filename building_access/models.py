
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Door(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    access_to_doors = models.ManyToManyField(Door)

    def __str__(self):
        return self.name

class Tag(models.Model):
    uid = models.BinaryField(max_length=10, unique=True)
    active = models.BooleanField(default=True)
    note = models.CharField(blank=True, max_length=128)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    access_to_doors = models.ManyToManyField(Door)
    groups_member = models.ManyToManyField(Group)

    def __str__(self):
        return self.uid + self.note
