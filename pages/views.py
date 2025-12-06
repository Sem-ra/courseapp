from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request,"pages/about.html")

def contact(request):
    return render(request,"pages/contact.html")

# render html sayfasıı gönderecek render(request,tamplate in ismi)
# ilk başta template klasörü eklenmeli ve altında index.html açılır
# settingse hmtl i eklemeliyiz
# sol alttaki settings açıldıktan sonra json logosuna tıklayıp oraya "emmet.includeLanguages": {"django-html":"html"}, eklemeliyiz html in çalışması için