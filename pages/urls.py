from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    path('hakkimizda/', views.about),
    path('iletisim/', views.contact),
    
    
]
