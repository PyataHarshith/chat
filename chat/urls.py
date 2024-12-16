from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:Room>/', views.Room, name='Room'),
    path('checkview',views.checkview, name='checkview'),
    path('send',views.send, name='send'),
    path('getroom/<str:Room>/', views.getroom, name='getroom'),
    path('getMessages/<str:Room>/', views.getMessages, name='getMessages')
]