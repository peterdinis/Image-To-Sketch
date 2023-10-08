from django.shortcuts import render
import cv2

def listAllSketches(request):
   return render(request, 'sketchs/list.html')

## Todo: Update later
def generateNewSketch(request):
    return render(request, 'sketchs/generate.html')