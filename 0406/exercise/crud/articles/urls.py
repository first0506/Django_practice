from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='index'),
    path('new_article/', views.new_article, name='new'),
    path('create_article/', views.create_article, name='create'),
    path('article_detail/<int:article_pk>/', views.article_detail, name='detail'),
    path('edit_article/<int:article_pk>/', views.edit_article, name='edit'),
    path('update_article/<int:article_pk>/', views.update_article, name='update'),
    path('delete_article/<int:article_pk>/', views.delete_article, name='delete'),
]