from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Anasayfa")

def hakkimizda(request):
    return HttpResponse("Hakkımızda Sayfası")

def iletisim(request):
    return HttpResponse("İletişim Sayfası")
