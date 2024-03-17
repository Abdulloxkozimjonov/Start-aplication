from django.shortcuts import render, redirect
from dashboard import models

def index_view(request):
    context = {
        'ad': models.Add.objects.all().order_by('-id')[:8]
    }
    return render(request, 'index.html', context)


def single_add(requet, pk):
    single_ad = models.Add.objects.get(pk=pk)
    context = {
        'single_ad': single_add
    }
    return render(request, 'poster-page.html', context)