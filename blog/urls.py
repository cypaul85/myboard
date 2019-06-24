from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list', views.list, name='list'),
    path('write', views.write, name='write'),
    path('detail', views.detail),
    path('edit', views.edit),
    path('update', views.update, name='update'),
    path('delete', views.delete),
]