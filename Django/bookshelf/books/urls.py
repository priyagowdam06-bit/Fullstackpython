from django.urls import path  # FIX 1: import path from django.urls
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_details, name='book_details'),
    path('book/add/', views.BookCreateView.as_view(), name='book_add'), # FIX 2: added comma here
    path('book/<int:pk>/review/', views.add_review, name='add_review'),
]