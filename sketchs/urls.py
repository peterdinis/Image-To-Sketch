from django.urls import path
from . import views

urlpatterns = [
    path("", views.listAllSketches, name="list_sketchs"),
    path('<slug:slug>', views.sketchDetail, name="sketch_detail"),
    path("generate/", views.generateNewSketch, name="sketch_generate")
]