
from django.urls import path
from .views import home, kurslar



urlpatterns = [
    path('',home),
    path('anasayfa',home),
    path('kurslar',kurslar),
]
