from . import views
from django.urls import path

app_name='madlib'
urlpatterns = [
    path('', views.index, name='index'),
    path('game1/', views.word_list, name='word_list'),
    path('gameview1.html/', views.gameview, name='gameview'),
    path('game2/', views.word_list2, name='word_list2'),
    path('gameview2.html/', views.gameview2, name='gameview2'),
    path('game3/', views.word_list3, name='word_list3'),
    path('gameview3.html/', views.gameview3, name='gameview3'),
    path('game4/', views.word_list4, name='word_list4'),
    path('gameview4.html/', views.gameview4, name='gameview4'),
    path('game5/', views.word_list5, name='word_list5'),
    path('gameview5.html/', views.gameview5, name='gameview5'),
    path('deletewords/', views.deletewords, name='deletewords')
]