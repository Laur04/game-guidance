from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('initial/', views.initial, name="initial"),
    path('recommendations/', views.recommendations, name='recommendations'),
    path('browse/', views.browse, name='browse'),
    path('user-games/', views.user_games, name='user-games'),
]
