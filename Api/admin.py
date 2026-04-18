from django.contrib import admin
from .models import Tasks,Tag,Category
admin.site.register(Tasks)
admin.site.register(Tag)
admin.site.register(Category)