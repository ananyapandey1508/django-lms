from django.shortcuts import render
from .models import Book

def index(request):
    return render(request, "index.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})
