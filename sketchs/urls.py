from django.urls import path
from . import views

urlpatterns = [
    path("generate/", views.generateNewSketch, name="sketch_generate"),
    path('list/', views.sketch_list, name='sketch_list'),
    path('sketches/search/', views.sketch_search, name='sketch_search'),
]