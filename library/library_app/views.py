from .models import Book

from django.contrib import messages

# Create your views here.
def index(request):
    test = {"test": "text"}
    context = { 'books': Book.objects.all() }
    return render(request, 'index.html', context)

def show(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    test = {'book': {'title' : book.title, 'author' : book.author}}
    return render(request, 'show.html', test)
    
def not_found_404(request, exception):
    data = { 'err': exception }
    return render(request, '404.html', data)
