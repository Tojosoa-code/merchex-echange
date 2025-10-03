"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.index, name="index"),
    path("bands/", views.band_list, name="band_list"),
    path("bands/<int:id>/", views.band_detail, name="band_detail"),
    path("bands/add/", views.band_create, name="band_create"),
    path("bands/update/<int:id>", views.band_update, name="band_update"),
    path("bands/delete/<int:id>", views.band_delete, name="band_delete"),
    path("about-us/", views.about, name="about"),
    path("contact-us/", views.contact, name="contact"),
    path("listes/", views.listing, name="listes"),
    path("listes/<int:id>/", views.list_detail, name="list_detail"),
    path("listes/add/", views.list_create, name="list_create"),
    path("listes/update/<int:id>", views.list_update, name="list_update"),
    path("listes/delete/<int:id>", views.list_delete, name="list_delete"),
    path("email-sent/", views.email_sent, name="email_sent"),
]
