from django.shortcuts import render
from .models import Sketch
import cv2

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
    # Read the original image
    image1 = cv2.imread('image.jpg')
    
    # Display the original image
    window_name = 'Actual image'
    cv2.imshow(window_name, image1)

    # Convert the image to grayscale
    grey_img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    
    # Invert the grayscale image
    invert = cv2.bitwise_not(grey_img)
    
    # Apply Gaussian blur to the inverted image
    blur = cv2.GaussianBlur(invert, (21, 21), 0)
    
    # Invert the blurred image
    invertedblur = cv2.bitwise_not(blur)
    
    # Create the sketch by dividing the grayscale image by the inverted blurred image
    sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
    
    # Save the sketch as "sketch.jpeg"
    cv2.imwrite("sketch.jpeg", sketch)
    
    # Read the saved sketch image
    image = cv2.imread("sketch.jpeg")
    
    # Display the sketch image
    window_name = 'Sketch image'
    cv2.imshow(window_name, image)
    
    # Wait for a key press and then close the OpenCV windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    # Render the Django template
    return render(request, 'sketchs/generate.html')