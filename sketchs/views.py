from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2


def listAllSketches(request):
   return render(request, 'sketchs/list.html')

## TODO: Broken and must be fixed
def generateNewSketch(request):
    if request.method == "POST":
        # Upload fotky
        image = request.FILES['image']
        fs = FileSystemStorage()
        file_name = fs.save(image.name, image)
        image_path = fs.url(file_name)

        # Vytvorenie skice
        try:
            sketch = cv2.imread(image)

            # Ak obrázok neexistuje alebo je poškodený, kód sa dostane sem.
            if sketch is None:
                raise Exception('The image file is empty or corrupted.')
        except FileNotFoundError:
            raise Exception('The image file does not exist.')
        except cv2.error:
            raise Exception('The image file is corrupted or in an unsupported format.')

        gray_img = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)
        invert = cv2.bitwise_not(gray_img)
        blur = cv2.GaussianBlur(invert, (21, 21), 0)
        inverted_blur = cv2.bitwise_not(blur)
        sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)

        # Uloženie skice
        cv2.imwrite("sketch.png", sketch)

        print(sketch)

        # Vrátenie upravenej fotky
        return HttpResponse(open("sketch.png", "rb").read())
        
    return render(request, 'sketchs/generate.html')
    if request.method == "POST":
        # Upload fotky
        image = request.FILES['image']
        fs = FileSystemStorage()
        file_name = fs.save(image.name, image)
        image_path = fs.url(file_name)

        # Vytvorenie skice
        try:
            sketch = cv2.imread(image_path)
        except FileNotFoundError:
            # The image file does not exist.
            return HttpResponse('The image file does not exist.')
        except cv2.error:
            # The image file is corrupted or in an unsupported format.
            return HttpResponse('The image file is corrupted or in an unsupported format.')

        if sketch is None:
            # The image file is empty.
            return HttpResponse('The image file is empty.')

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