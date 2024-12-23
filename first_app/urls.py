from django.urls import path

from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index1', views.index1, name='index1'),
    path('index2', views.index2, name='index2'),
]
