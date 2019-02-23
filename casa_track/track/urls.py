from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('tracking/', views.tracking, name='tracking'),
    path('delete_form', views.delete_form, name='delete_form'),
]
