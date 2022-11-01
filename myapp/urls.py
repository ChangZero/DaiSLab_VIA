from django.urls import path
from . import views

urlpatterns = [
    path('via/', views.viaindex, name='via-index'),
    path('', views.index, name='myapp-index')
]
