from django.shortcuts import render
from blog.models import Feedback

from django.http import HttpResponse

def index(request):
    thank = False
    if request.method=="POST":
        email = request.POST.get('email', '')
        desc = request.POST.get('desc', '')
        index = Feedback(email=email,desc=desc)
        index.save()
        thank = True
    return render(request, 'adoptme/index.html', {'thank': thank})

