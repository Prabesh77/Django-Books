from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import addBook

# Create your views here.

def books_view(request):
    items = addBook.objects.all()
    return render(request, 'Books_app/base.html', {'all_items': items})

def addBooks(request):
    new_item = addBook(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/book/')

def deleteBooks(request, book_id):
    delete_item = addBook.objects.get(id=book_id)
    delete_item.delete()
  
    return HttpResponseRedirect('/book/')


