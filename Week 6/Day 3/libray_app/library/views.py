from django.shortcuts import render

books = [
    {"id": 1, "title": "SQL503", "author": "Sarah", "year": 2026},
    {"id": 2, "title": "Wep Development111", "author": "Mshael", "year": 2026},
    {"id": 3, "title": "Learning Django509", "author": "Dalal", "year": 2026},
    {"id": 4, "title": "FastAPI511", "author": "Taif", "year": 2026},
]

def book_list(request):
    return render(request, 'library/book_list.html', {'books': books})

def book_detail(request, id):
    book = books[id -1]
    return render(request, 'library/book_detail.html', {'book': book})