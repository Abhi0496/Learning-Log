from django.shortcuts import render

# Create your views here.
#it takes info from requests, prepares the data needed to generate a page, and then sends the data back to the browser

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')