from django.urls import path

from . import views

urlpatterns = [
    path('', views.AddEmailFunc, name='notifications-notifications'),
    path('admin/email/', views.AdminNotify, name='notifications-adminnotify')
]
