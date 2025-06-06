from django.urls import path,include
from .import views 


urlpatterns = [
    path('', views.home, name="homepage"),
    path('home/',views.home,name="home"), 
    path('about/',views.about,name="aboutpage"),
    path('form/',views.submit_form,name="formpage"),
    # path('djangoform/',views.Django_form,name="djangoform"),
    # path('djangoform/',views.student_form,name="djangoform")
    path('djangoform/',views.password_check,name="djangoform")
   
]