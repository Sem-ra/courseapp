from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
# def home(request):
#     return HttpResponse("Anasayfa")
data={
    "programlama":"programalama kategorisine ait kurslar",
    "web-gelistirme":"web geliştirme kategorisine ait kurslar",
    "mobil":"mobil kategorisine ait kurslar"
}
def index(request):
    return render(request,'courses/index.html')
# index in başına courses eklememizin sebebi aynı html ismi olduğunda 
# kendi klösründe bulamazsa alt uygulamalrda arar bunun önüne geçmek için template klasörü
# aştına courses klasörü açıp index.html içerisine atıyoruz. böylece alt uygulamalrda arayamıyor

# def kurslar(request):
#     return render(request,"courses/index.html")
def kurslar(request):
    list_items=""
    category_list=list(data.keys())
    redirect_url=reverse('courses_by_category', args=[category])
    for category in category_list:
        list_items+=f"<li><a href='{redirect_url}'>{category}</a></li> "

    html=f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)
# Bu zor olan şekli html yi ayrı bir yerde yapıp değişecek kısımları işaretleyip yapmak daha kolay
# Yani sitedeki html yi oluşturan etiketler aynı datalar farklı.

    

# def programlama(request):
#     return HttpResponse("Programlama Kursları")

# def mobiluygulamalar(request):
#     return HttpResponse("Mobil Uygulamalar")

# def kurslar(request):
#     category=list(data.keys())
# for category in category_list:
#     redirect_url=reverse('course_by_category', args=[category])
#     list
                

def details(request, kurs_adi):
    return HttpResponse(f"{kurs_adi} , Kurs Detayları")

def getCoursesByCategory(request, category_name):
    try:
        category_text=data[category_name]
        return HttpResponse(category_text)
    except:
        return HttpResponseNotFound("yanlış kategori seçimi")


    # if(category_name=="programlama"):
    #     text="Programlama Kursları"
    # elif(category_name=="web-gelistirme"):
    #     text="Web Geliştirme Kursları"
    # else:
    #     text="Yanlış Kategori"
    # return HttpResponse(text)  
def getCoursesByCategoryId(request, category_id):
    # return HttpResponse(f"{category_id} , ID'li Kategoriye Ait Kurslar")
    category_list=list(data.keys())
    if(category_id>len(category_list)):
        return HttpResponseNotFound("Yanlış Kategori ID'si")
    category_name=category_list[category_id-1]
    redirect_url=reverse('courses_by_category', args=[category_name])
    return redirect(redirect_url)
    
    # return redirect('/kurs/kategori/'+redirect_text)