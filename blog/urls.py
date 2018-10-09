from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:post_id>', views.detail, name='detail'),
] 
