from django.shortcuts import render
from premiers.models import Premier
from films.models import Film
from cartoons.models import Cartoon
from series.models import Serie
from home.models import Advertisement
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def home(request):
    latest_advertisements_list = Advertisement.objects.order_by('-pub_date')[:6]
    latest_premiers_list = Premier.objects.order_by('-pub_date')[:6]
    latest_films_list = Film.objects.order_by('-pub_date')[:6]
    latest_cartoons_list = Cartoon.objects.order_by('-pub_date')[:6]
    latest_series_list = Serie.objects.order_by('-pub_date')[:6]
    return render(request, "home/home.html",
                  {'latest_advertisements_list': latest_advertisements_list,
                   'latest_premiers_list': latest_premiers_list,
                   'latest_films_list': latest_films_list,
                   'latest_series_list': latest_series_list,
                   'latest_cartoons_list': latest_cartoons_list})


