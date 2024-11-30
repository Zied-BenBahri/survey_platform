from django.urls import path
from .views import enquete_detail, enquete_list,enquete_create,load_localites,enquete_map
from django.contrib import admin


app_name = "enquete"
urlpatterns = [
    path('list',enquete_list, name ='enquete_list'),
    path('create',enquete_create),
    path('<int:pk>',enquete_detail),
    path('load-localites/', load_localites, name='load_localites'),
    path('map',enquete_map)
]
