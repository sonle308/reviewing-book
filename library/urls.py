from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('books/rating', views.rating_book, name='rating_book'),
    path('books/reading', views.reading_book, name='reading_book'),
    path('books/favorite', views.favorite_book, name='favorite_book'),
    path('books/read', views.read_book, name='read_book'),
]
