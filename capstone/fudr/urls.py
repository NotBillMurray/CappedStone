from django.urls import path
from . import views

app_name='fudr'
urlpatterns = [
    path('', views.index, name='index')
]