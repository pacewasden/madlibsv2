from . import views
from django.urls import path

app_name='words'
urlpatterns = [
    path('game1/', views.delete_word, name="delete_word")
]