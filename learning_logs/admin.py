from django.contrib import admin
from .models import Topic
# Register your models here.

admin.site.register(Topic)

#it imports the model we want to register, Topic.
#the dot in front of models tells Django to look for models.py in the same directory as admin.py
#The code admin.site.register() tells Django to manage our model through the admin site