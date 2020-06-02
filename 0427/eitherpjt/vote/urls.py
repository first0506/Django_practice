from django.urls import path
from . import views

app_name = 'vote'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('<int:vote_pk>/', views.detail, name='detail'),
    path('<int:vote_pk>/comments/', views.comments_create, name='comments_create'),
    path('random/', views.random, name='random'),
]