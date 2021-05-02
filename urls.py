from django.contrib import admin
from django.urls import path

from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index', views.index, name="index"),
    path('location', views.location, name='location'),
    path('go', views.go, name='go'),
    path('speech', views.speech, name='speech'),
    path('conver', views.conver, name='conver'),
    path('trans', views.trans, name='trans'),
    path('chatbot', views.chatbot, name='chatbot'),
    path('chat', views.chat, name='chat'),
]