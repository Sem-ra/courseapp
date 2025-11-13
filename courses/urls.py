
from django.urls import path
from .import views 



urlpatterns = [
    # path('',views.home),
    # path('anasayfa',views.home),
    path('',views.kurslar),
    path('list',views.kurslar),
    path('<kurs_adi>', views.details),
    # # path('programlama',views.programlama),
    # # path('mobil-uygulamalar',views.mobiluygulamalar),
    path('kategori/<int:category_id>',views.getCoursesByCategoryId),
    path('kategori/<str:category_name>',views.getCoursesByCategory,name='courses_by_category'),
    

]
#inputlar url de hep str olduğu için intleri algılaması için int i önce yazmalıyız. eğer str tanımladığımızı önce yazarsak hiç bir zaman int i algılamaz.
#<> olan tanımlandıktan sonra alttakilere gitmesi için alttaki <> lere bir anahtar kelime tanımlıyoruz. kategori/ gibi.