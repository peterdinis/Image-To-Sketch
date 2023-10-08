from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2


def listAllSketches(request):
   return render(request, 'sketchs/list.html')

def generateNewSketch(request):
    if request.method == "POST":
        # Upload fotky
        image = request.FILES['image']
        fs = FileSystemStorage()
        file_name = fs.save(image.name, image)
        image_path = fs.url(file_name)

        # Vytvorenie skice
        sketch = cv2.imread(image_path)
        gray_img = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)
        invert = cv2.bitwise_not(gray_img)
        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        inverted_blur = cv2.bitwise_not(blur)
        sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)

        # Uloženie skice
        cv2.imwrite("sketch.png", sketch)

        # Vrátenie upravenej fotky
        return HttpResponse(open("sketch.png", "rb").read())
        
    return render(request, 'sketchs/generate.html')