from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.sketch_list, name='sketch_list'),
    path('search/', views.sketch_search, name='sketch_search'),
    path('generate/', views.generate_sketch, name='generate_sketch')
]