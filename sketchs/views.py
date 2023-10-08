from django.shortcuts import render
import cv2

def listAllSketches(request):
   return render(request, 'sketchs/list.html')

## Todo: Update later
def generate_new_sketch(request):
    """Generates a new sketch from an image.

    Args:
        request: A Django HttpRequest object.

    Returns:
        A Django HttpResponse object.
    """

    # Load the image.
    image = cv2.imread('Image.jpg')

    # Convert the image to grayscale.
    gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Invert the image.
    invert = cv2.bitwise_not(gray_img)

    # Smooth the image with Gaussian blur.
    blur = cv2.GaussianBlur(invert, (21, 21), 0)

    # Invert the blurred image.
    inverted_blur = cv2.bitwise_not(blur)

    # Divide the original grayscale image by the inverted blurred image to create the sketch.
    sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)

    # Save the sketch image.
    cv2.imwrite("sketch.png", sketch)

    # Return the HTML response.
    return render(request, 'sketchs/generate.html')