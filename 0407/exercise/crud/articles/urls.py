from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='index'),
    path('new_article/', views.create_article, name='new'),
    path('article_detail/<int:article_pk>/', views.article_detail, name='detail'),
    path('article_update/<int:article_pk>/', views.update_article, name='update'),
    path('article_delete/<int:article_pk>/', views.delete_article, name='delete'),
]