from django.urls import path

from . import views

urlpatterns = [
    path('<int:page>/', views.home, name='blog-home'),
    path('post/<id>/', views.post, name='blog-post'),
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('music/', views.music, name='blog-music')


]


# app/model_viewtype.html
# example: blog/post_list.html but you can change this in views.py with the template_name feature in a class such as ListView
