from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import cv2
from .forms import SketchForm
from .models import Sketch

def sketch_list(request):
    sketches = Sketch.objects.all()
    sutff_for_frontend = {
        'sketches': sketches
    }
    return render(request, 'sketchs/lists.html', sutff_for_frontend)

def generateNewSketch(request):
    if request.method == "POST":
        form = SketchForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                # Save the uploaded image
                sketch = form.save(commit=False)

                # Create the sketch
                image_path = sketch.image.path
                sketch_image = cv2.imread(image_path)
                gray_img = cv2.cvtColor(sketch_image, cv2.COLOR_BGR2GRAY)
                invert = cv2.bitwise_not(gray_img)
                blur = cv2.GaussianBlur(invert, (21, 21), 0)
                inverted_blur = cv2.bitwise_not(blur)
                sketch_image = cv2.divide(gray_img, inverted_blur, scale=256.0)

                # Save the sketch
                sketch_filename = "sketch.png"
                cv2.imwrite(sketch_filename, sketch_image)

                sketch.image.name = sketch_filename
                sketch.save()

                # Clean up temporary files
                fs = FileSystemStorage()
                fs.delete(sketch_filename)

                return redirect('listAllSketches')  # Redirect to a list of sketches

            except cv2.error:
                return HttpResponse('The image file is corrupted or in an unsupported format.', status=400)

    else:
        form = SketchForm()

    return render(request, 'sketchs/generate.html', {'form': form})
    sketch = None

    if request.method == "POST" and 'image' in request.FILES:
        try:
            # Upload and save the image
            image = request.FILES['image']
            fs = FileSystemStorage()
            file_name = fs.save(image.name, image)
            image_path = fs.url(file_name)

            # Debug: Print the file size and image path
            print(f"File Size: {image.size} bytes")
            print(f"Image Path: {image_path}")

            # Create the sketch
            sketch = cv2.imread(image_path)
            
            if sketch is None:
                raise Exception('The image file is empty or corrupted.')

            gray_img = cv2.cvtColor(sketch, cv2.COLOR_BGR2GRAY)
            invert = cv2.bitwise_not(gray_img)
            blur = cv2.GaussianBlur(invert, (21, 21), 0)
            inverted_blur = cv2.bitwise_not(blur)
            sketch = cv2.divide(gray_img, inverted_blur, scale=256.0)

            # Save the sketch
            sketch_filename = "sketch.png"
            cv2.imwrite(sketch_filename, sketch)

            # Return the sketch as an HTTP response
            with open(sketch_filename, "rb") as sketch_file:
                response = HttpResponse(sketch_file.read(), content_type="image/png")

            # Clean up temporary files
            fs.delete(file_name)
            fs.delete(sketch_filename)

            return response

        except FileNotFoundError:
            return HttpResponse('The image file does not exist.', status=400)
        except cv2.error:
            return HttpResponse('The image file is corrupted or in an unsupported format.', status=400)

    return render(request, 'sketchs/generate.html', {'sketch': sketch})