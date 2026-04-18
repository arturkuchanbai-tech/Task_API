from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Tasks(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    create = models.DateTimeField(auto_now_add=True)
    categori = models.ForeignKey(Category,on_delete=models.CASCADE, null=True, blank=True)
    tags = models.ManyToManyField('Tag' ,blank=True)

    def __str__(self):
        return self.titile

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
