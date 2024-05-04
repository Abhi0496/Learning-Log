from django.shortcuts import render
from .models import Topic

# Create your views here.
#it takes info from requests, prepares the data needed to generate a page, and then sends the data back to the browser

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    "Showing single topic and all its entries"
    topic = Topic.objects.get(id=topic_id) #queries
    entries = topic.entry_set.order_by('-date_added') #queries
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)