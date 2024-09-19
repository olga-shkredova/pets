from django.http import HttpResponse
from django.shortcuts import render
from .models import Cats


def cats_(request):
    cats = Cats.objects.all()
    context = {
        'cats': cats
    }
    return render(request, 'cats.html', context)
