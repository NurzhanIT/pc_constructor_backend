import uuid

from django.db import models
from django.contrib.auth.models import User

from pc_components.models import MonitorItemModel


# Create your models here.


class UsersPcModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=15)
    user = models.ForeignKey(User, auto_created=True, on_delete=models.CASCADE)
    createdAt = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title


class UserMonitorModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    related_item = models.ForeignKey(UsersPcModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    short_description = models.TextField(max_length=5000, null=True)
    price = models.CharField(max_length=20)
    diagonal = models.CharField(max_length=5, null=False)
    width = models.CharField(max_length=5, null=True)
    height = models.CharField(max_length=5, null=True)
    matrix_type = models.CharField(max_length=10, null=True)
    screen_resolution = models.CharField(max_length=20, null=True)
    fps = models.CharField(max_length=10, null=True)
    monitor_class = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class UserVideoCardModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    related_item = models.ForeignKey(UsersPcModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    short_description = models.TextField(max_length=5000, null=True)
    price = models.CharField(max_length=20)
    video_memory = models.CharField(max_length=15, null=False)
    video_memory_type = models.CharField(max_length=15, null=False)
    base_frequency = models.CharField(max_length=20)
    max_frequency = models.CharField(max_length=20)
    video_memory_frequency = models.CharField(max_length=20)
    gpu_type = models.CharField(max_length=20)
    taken_slots_num = models.CharField(max_length=20)
    technical_process = models.CharField(max_length=20)
    manufacturer = models.CharField(max_length=20)
    recommended_computer_power_supply = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name
