from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracking, name='tracking'),
    path('delete/', views.delete_form, name='delete_form'),
]
