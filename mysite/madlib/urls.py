from . import views
from django.urls import path

app_name='madlib'
urlpatterns = [
    path('', views.index, name='index'),
    path('game1/', views.word_list, name='word_list'),
    path('gameview1.html/', views.gameview, name='gameview'),
    path('deletewords/', views.deletewords, name='deletewords')
]