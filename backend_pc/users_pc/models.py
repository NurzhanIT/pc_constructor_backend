from django.db import models

from pc_components.models import PcComponentModel
from django.contrib.auth.models import User

# Create your models here.


class UsersPCModel(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    lastUpdateAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, auto_created=True,on_delete=models.CASCADE)
    class Meta:
        ordering = ['-createdAt']


class UserPCItemModel(models.Model):
    pc = models.ForeignKey(UsersPCModel, on_delete=models.CASCADE)
    component = models.ManyToManyField(PcComponentModel)