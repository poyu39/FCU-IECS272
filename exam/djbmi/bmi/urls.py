from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.main, name='main'),
    path('people/', views.allpeople, name='index'),
    path('people/details/<slug:ssn>', views.details, name='details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)