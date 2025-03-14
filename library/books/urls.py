from books.views import BookAPIView, AuthorAPIView, BookDetailAPIView, AuthorDetailAPIView
from books import views 
from django.urls import path

urlpatterns = [
    
    path("", views.home, name="home"),
    path('books/', BookAPIView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailAPIView.as_view()),
    path('authors/', AuthorAPIView.as_view(), name='authors'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view())
    
]