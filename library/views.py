from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Book, UserBook
import json
from django.core import serializers

def landing_page(request):
    userId = request.user.id
    books = Book.objects.filter(userbook__user_id=userId).values('id',
                                                                 'title',
                                                                 'description',
                                                                 'image',
                                                                 'rating',
                                                                 'userbook__is_favorite',
                                                                 'userbook__is_reading'   
                                                                )
    return render(request, 'library/landing_page.html', {'user': request.user, 'books': books})

def rating_book(request):
    data = json.loads(request.body)
    score = data["score"]
    bookId = data["bookId"]
    userId = request.user.id
    try:
        userBook = UserBook.objects.get(user_id=userId, book_id=bookId)
    except Exception as e:
        userBook = UserBook.objects.create(user_id=userId, book_id=bookId)
    userBook.rating = score
    userBook.save()

    return HttpResponse(True)

def reading_book(request):
    data = json.loads(request.body)
    isReading = data["isReading"]
    bookId = data["bookId"]
    userId = request.user.id
    try:
        userBook = UserBook.objects.get(user_id=userId, book_id=bookId)
    except Exception as e:
        userBook = UserBook.objects.create(user_id=userId, book_id=bookId)
    userBook.is_reading = isReading
    userBook.save()

    return HttpResponse(True)

def favorite_book(request):
    data = json.loads(request.body)
    isFavorite = data["isFavorite"]
    bookId = data["bookId"]
    userId = request.user.id
    try:
        userBook = UserBook.objects.get(user_id=userId, book_id=bookId)
    except Exception as e:
        userBook = UserBook.objects.create(user_id=userId, book_id=bookId)
    userBook.is_favorite = isFavorite
    userBook.save()

    return HttpResponse(True)
