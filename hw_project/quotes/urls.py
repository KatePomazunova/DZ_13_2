from django.urls import path

from . import views

app_name = "quotes"

urlpatterns = [
    path('', views.main, name="main"),
    path('<int:page>', views.main, name="root-paginate"),
    path('author/<int:_id>', views.author_about, name='author'),
    path('add_author', views.add_author, name='add_author'),
    path('add_quote/', views.add_quote, name='add_quote'),
    path('tag/<str:tag>/', views.tag_quotes, name='tag_quotes')]

