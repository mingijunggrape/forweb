from django.urls import path
from . import views
from .models import Board
urlpatterns = [
    path('', views.index, name='index'),
    path('Boardindex/<int:number>/', views.Boardindex, name='Boardindex'),
    path('login', views.login, name='login'),
    path('sign', views.sign, name='sign'),
    path('logout', views.logout, name='logout'),
    path('comment_remove/<int:pk>', views.comment_remove, name='comment_remove'),
    path('docterlist/<str:name>/', views.docterlist, name='docterlist'),
    path('write/', views.write, name='write'),
    path('free/', views.free, name='free'), 
    path('pc/', views.pc, name='pc'), 
    path('moblie/', views.moblie, name='moblie'), 
    path('embed/', views.embed, name='embed'), 
    path('anti/', views.anti, name='anti'),
    path('notice/', views.ItisNotice, name='ItisNotice'), 
    
]
