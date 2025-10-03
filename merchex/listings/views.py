from django.shortcuts import render
from listings.models import Band, Listing
from listings.forms import ContactUsForm, BandForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect


def index(request):
    return render(request, "listings/index.html")


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})


def about(request):
    return render(request, "listings/about.html")


def listing(request):
    lists = Listing.objects.all()
    return render(request, "listings/listes.html", {"listes": lists})


def list_detail(request, id):
    list = Listing.objects.get(id=id)
    return render(request, "listings/list_detail.html", {"list": list})


def contact(request):
    print("La méthode de requête est : ", request.method)
    print("Les données POST sont : ", request.POST)

    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data["message"],
                from_email=form.cleaned_data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("email_sent")
    else:
        form = ContactUsForm()
    return render(request, "listings/contact.html", {"form": form})


def email_sent(request):
    return render(request, "listings/email_sent.html")


def band_create(request):

    if request.method == "POST":
        bandForm = BandForm(request.POST)
        if bandForm.is_valid():
            bandForm.save()
            return redirect("band_list")
    else:
        bandForm = BandForm()
    return render(request, "listings/band_create.html", {"form": bandForm})


def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == "POST":
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect("band_detail", band.id)
    else:
        form = BandForm(instance=band)
    return render(request, "listings/band_update.html", {"form": form, "band": band})


def list_create(request):

    if request.method == "POST":
        listingForm = ListingForm(request.POST)
        if listingForm.is_valid():
            listingForm.save()
            return redirect("listes")
    else:
        listingForm = ListingForm()
    return render(request, "listings/list_create.html", {"form": listingForm})


def list_update(request, id):

    listing = Listing.objects.get(id=id)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect("list_detail", listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(
        request, "listings/list_update.html", {"form": form, "listing": listing}
    )


def list_delete(request, id):
    listing = Listing.objects.get(id=id)

    if request.method == "POST":
        listing.delete()
        return redirect("listes")

    return render(request, "listings/list_delete.html", {"listing": listing})


def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == "POST":
        band.delete()
        return redirect("band_list")

    return render(request, "listings/band_delete.html", {"band": band})
