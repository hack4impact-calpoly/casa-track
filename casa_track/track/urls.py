from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tracking/', views.tracking),
]
