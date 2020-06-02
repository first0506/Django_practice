from  django.urls import path
from . import views

app_name = 'musics'
urlpatterns = [
    # 'api/v1/musics/'
    path('musics/', views.music_list, name='music_list'),
]