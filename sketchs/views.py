from django.shortcuts import render
from .models import Sketch
import cv2
import os
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def sketch_list(request):
    sketches = Sketch.objects.all()
    page_num = request.GET.get('page', 1)
    paginator = Paginator(sketches, 10)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    sutff_for_frontend = {
        'sketches': sketches,
        "page_obj": page_obj
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
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
        if uploaded_image.name.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Save the uploaded image
            media_root = settings.MEDIA_ROOT
            image_path = os.path.join(media_root, 'uploaded_image.jpg')
            with open(image_path, 'wb') as f:
                for chunk in uploaded_image.chunks():
                    f.write(chunk)

            # Process the uploaded image
            image1 = cv2.imread(image_path)
            if image1 is not None:
                grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
                invert = cv2.bitwise_not(grey_img)
                blur = cv2.GaussianBlur(invert, (21, 21), 0)
                invertedblur = cv2.bitwise_not(blur)
                sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

                # Save the generated sketch image
                sketch_path = os.path.join(media_root, 'sketch.jpeg')
                cv2.imwrite(sketch_path, sketch)

                return render(request, 'sketchs/generate.html', {'sketch_path': 'media/sketch.jpeg'})
            else:
                # Handle the case where image loading failed
                return render(request, 'sketchs/error.html')

        else:
            # Handle invalid file type
            return render(request, 'sketchs/error.html')

    return render(request, 'sketchs/generate.html')