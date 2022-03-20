from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='Home page'),
    path('about/', views.about,name='About page'),
    path('contact/', views.contact,name='Contact page'),
]
