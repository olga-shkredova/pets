from django.http import HttpResponse
from django.shortcuts import render
from .models import Dogs


def dogs_(request):
    dogs = Dogs.objects.all()
    context = {
        'dogs': dogs
    }
    return render(request, 'dogs.html', context)
