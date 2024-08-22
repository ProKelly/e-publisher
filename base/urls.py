from django.urls import path
from . import views


urlpatterns = [
    path('publishers/', views.PublisherListView.as_view()),
    path('publishers/<str:pk>/detail/', views.PublisherDetailView.as_view(), name='publisher-detail'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<str:pk>/detail/', views.BookDetailView.as_view(), name='book-detail'),
]
