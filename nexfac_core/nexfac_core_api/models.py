from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    task_inputs = models.JSONField(null=True)
    independent_task = models.BooleanField(null=True)

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.name


class Area(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    assets = models.ManyToManyField(Asset)
    areas = models.ManyToManyField(Area)
    
    def __str__(self):
        return self.name


