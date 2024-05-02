from django.db import models

# Create your models here.
# We will define the data we want to manage in our app
# We(user) will create multiple topic in learning log and and the entry they will make will be tied to a topic
# We will also store timestamp of each entry
#Hello


class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returning string representation of Model"""
        return self.text

    """
    If a model has a __str__() method, 
    Django calls that method whenever it needs to generate output referring to an instance of that model
    """
