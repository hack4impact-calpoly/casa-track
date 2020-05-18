from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracking, name='tracking'),
    path('success/', views.success, name='success'),
    path('delete/', views.delete_form, name='delete_form'),
    path('supervisor_confirm/<int:pk>', views.supervisor_confirm, name= "supervisor_confirm"),
    path('supervisor-success/', views.supervisor_success, name="supervisor_success"),
]
