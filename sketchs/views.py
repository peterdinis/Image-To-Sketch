from django.shortcuts import render
from .models import Sketch

def sketch_list(request):
    sketches = Sketch.objects.all()
    sutff_for_frontend = {
        'sketches': sketches
    }
    return render(request, 'sketchs/lists.html', sutff_for_frontend)

def sketch_search(request):
    query = request.GET.get('q', '')
    sketches = Sketch.objects.filter(name__icontains=query)
    stuff_for_frontend = {
        'sketches': sketches,
        'query': query
    }
    return render(request, 'sketchs/search.html', stuff_for_frontend)


def generate_sketch(request):
    return render(request, 'sketchs/generate.html')