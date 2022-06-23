from django.urls import path
from libmanage import views

urlpatterns = [
    path('', views.library, name = 'library'),
    path('home', views.home, name = 'home'),
    path('home/delete/<int:id>', views.delete_book, name = 'delete_book'),
    path('home/edit/<int:id>', views.edit_book, name = 'edit_book'),
    path('collection', views.collection, name = 'collection'),
    path('contact', views.contact, name = 'contact'),
    path('home/Addbook', views.Addbook, name = 'Addbook')
]