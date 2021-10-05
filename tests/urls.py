
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
 
    path('',views.home,name='home'),
    path('yearbook/',views.yearbook,name='yearbook'),
    path('profile/',views.profile,name='profile'),
    
]
