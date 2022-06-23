from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def library(request):
    context = {
        'welcome_text' : 'library',
    }
    return render (request, 'library.html', context)


def collection(request):
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 4)
    page = request.GET.get('pg')
    all_books = paginator.get_page(page)
   
    return render (request, 'collection.html', {'all_books': all_books})

@login_required
def home(request):
    all_books = Book.objects.all()
    paginator = Paginator(all_books, 4)
    page = request.GET.get('pg')
    all_books = paginator.get_page(page)
    return render (request, 'home.html', {'all_books': all_books})

@login_required
def  delete_book(request, id):
    book = Book.objects.get(pk=id)
    book.delete()
    return redirect('home')

@login_required
def  edit_book(request, id):
    if request.method == "POST":
        book = Book.objects.get(pk=id)
        form = BookForm(request.POST or None, instance = book)
        if form.is_valid():
            form.save()
        messages.success(request,("Book Edited"))   
        return redirect ('home')    
    else:
        book_obj = Book.objects.get(pk=id)
        return render (request, 'edit.html', {'book_obj':book_obj})      
    

def contact(request):
    context = {
        'welcome_text' : 'contact',
    }
    return render (request, 'contact.html', context)

@login_required
def Addbook(request):
    if request.method == "POST":
        form = BookForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request,("New book added"))   
        return redirect ('home')    
    else:
       return render (request, 'Addbook.html', {})    


       