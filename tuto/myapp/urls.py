from django.urls import path
from .import views

urlpatterns = [
    path('test', views.home,name='Home page'),
    path('about/', views.about,name='About page'),
    path('contact/', views.contact,name='About page'),
]
