from django.http import HttpResponse
from django.shortcuts import render
from .models import Eagles


def eagles_(request):
    eagles = Eagles.objects.all()
    context = {
        'eagles': eagles
    }
    return render(request, 'eagles.html', context)
