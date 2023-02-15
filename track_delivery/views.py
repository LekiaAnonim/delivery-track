from django.shortcuts import render, get_object_or_404
from .models import Package
from django.http import JsonResponse, HttpResponse
from django.template import loader


# Create your views here.
def index(request):

    context = {
    }
    return render(request, 'index.html', context)


def track_package(request):

    
    if request.method == 'GET':
        search = request.GET.get("search")
        package = Package.objects.filter(track_id=search)
        context = {
            'package': package,
        }
    return render(request, 'track_result.html', context)
