from django.urls import path
from . import views
urlpatterns = [
    path('', views.blog, name='blog'),
    path('example/', views.example, name='exemplo'),
]
