from django.shortcuts import render, HttpResponse
from time import gmtime, strftime
import os, time

# Create your views here.
def index(request):
    os.environ['TZ'] = 'US/Eastern'
    time.tzset()
    context = {
        "time": time.strftime("%b %d, %Y %I:%M %p")
    }
    return render(request, "index.html", context)
