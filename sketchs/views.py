from django.shortcuts import render
import cv2
import os

# Assuming 'Image.jpg' is in the same directory as your views.py file
image_path = os.path.join(os.path.dirname(__file__), 'Image.jpg')


def listAllSketches(request):
   return render(request, 'sketchs/list.html')

def sketchDetail(request):
    return render(request, 'sketchs/detail.html')

## Todo: Update later
def generateNewSketch(request):
    # Check if the HTTP request is a POST request
    if request.method == 'POST':
        # Load the image from the specified file
        image = cv2.imread(image_path)

        if image is not None:
            # Convert the image to grayscale
            grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Invert the grayscale image
            invert = cv2.bitwise_not(grey_img)

            # Apply Gaussian blur to smooth the image
            blur = cv2.GaussianBlur(invert, (21, 21), 0)

            # Invert the blurred image
            invertedblur = cv2.bitwise_not(blur)

            # Divide the grayscale image by the inverted blurred image to create the sketch
            sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

            # Save the generated sketch as 'sketch.png' in the same directory
            cv2.imwrite(os.path.join(os.path.dirname(__file__), 'sketch.png'), sketch)

            return render(request, 'sketch_result.html', {'sketch_generated': True})
        else:
            return render(request, 'sketch_result.html', {'sketch_generated': False})

    return render(request, 'generate_sketch.html')