from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Publisher, Book, Author
from django.utils import timezone

class PublisherListView(ListView):
    model = Publisher
    template_name = "base/publisher_list.html"
    context_object_name = "publishers"

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = "base/publisher_detail.html"
    context_object_name = "publisher"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context

class BookListView(ListView):
    queryset = Book.objects.order_by("-publication_date")
    context_object_name = 'books'
    template_name = 'base/book_list.html'

class BookDetailView(DetailView):
    model = Book 
    template_name = 'base/book_detail.html'
    context_object_name = 'book'


class PublisherBookListView(ListView):
    template_name = 'base/publisher_book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
    
    #adding get_context_data method because we also need the publisher on the template not only the books filtered abover in the get_queryset method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publisher'] = self.publisher
        return context

class AuthorDetailView(DetailView):
    queryset = Author.objects.all() # or model = Author
    template_name = 'base/author_detail.html'
    context_object_name = 'author'

    def get_object(self):
        obj = super().get_object()
        obj.last_accessed = timezone.now()
        obj.save()
        return obj