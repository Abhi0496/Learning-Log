"""Defining URL patterns for learning logs"""

#path function is needed when mapping URLs to views hence we have to import it
from django.urls import path
from . import views #dot refers to current directory so importing views from current directory

app_name = 'learning_logs'

#list of individual pages that can be requested from the learning_logs app
"""
path function takes 3 arguments
    1) String tht helps Django route the current request properly
    2) Specifies which function to call in views.py
    3) Provides name index for this URL pattern so we can refer to it more easily in other files throughout the project
"""
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Path to show all topics.
    path('topics/', views.topics, name='topics'),
    #Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
