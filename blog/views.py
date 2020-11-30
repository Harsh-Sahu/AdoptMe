from django.shortcuts import render
from .models import Donate,Pets
from math import ceil
# Create your views here.
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def findapet(request):
    allPets = []
    breeadinfo = Pets.objects.values('breead', 'id')
    cats = {item['breead'] for item in breeadinfo}
    for cat in cats:
        prod = Pets.objects.filter(breead=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allPets.append([prod, range(1, nSlides), nSlides])
    params = {'allPets':allPets}
    return render(request, 'blog/findapet.html', params)

def adoptioninfo(request):
    return render(request, 'blog/adoptioninfo.html')

def donate(request):
    thank = False
    if request.method=="POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        country= request.POST.get('country', '')
        donate = Donate(fname =fname,lname=lname, email=email, address=address,country=country)
        donate.save()
        thank = True
    return render(request, 'blog/donate.html', {'thank': thank})