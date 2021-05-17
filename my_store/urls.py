from django.urls import path

from my_store import views

urlpatterns = [
    path('', views.index, name='index')
]
