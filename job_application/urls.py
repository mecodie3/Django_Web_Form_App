from django.urls import path
from . import views

#django will look for that variable
#'' stands for home page
urlpatterns = [
    path('',views.index, name='index'),
    path('about/',views.about, name='about')
]