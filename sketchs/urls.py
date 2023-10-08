from django.urls import path
from . import views

urlpatterns = [
    path("", views.listAllSketches, name="list_sketchs"),
    path("generate/", views.generateNewSketch, name="sketch_generate")
]