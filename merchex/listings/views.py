from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band, Listing


def index(request):
    bands = Band.objects.all()
    return render(request, "listings/index.html", {"bands": bands})


def about(request):
    return render(request, "listings/about.html")


def listing(request):
    lists = Listing.objects.all()
    return render(request, "listings/listes.html", {"listes": lists})


def contact(request):
    return render(request, "listings/contact.html")
