from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('people/', views.allpeople, name='index'),
    path('people/details/<slug:ssn>', views.details, name='details'),
]