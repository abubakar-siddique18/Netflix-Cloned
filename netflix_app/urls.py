from django.urls import path
from .views import *

urlpatterns = [
     path('', home, name='home'),
    path('index/', index, name='index'),
   
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    
    path('logout/', login, name='logout'),
    path('movie/<str:pk>/', movie, name='movie'),
    path('genre/<str:pk>/', genre, name='genre'),
    path('add-to-list', add_to_list, name='add-to-list'),
    path('my-list', my_list, name='my-list'),
    path('index/search', search, name='search'),

]