from django.urls import path
from . import views


# set the 'app_name' to namespaceing in urls!!!
app_name = 'my_library'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("books/", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("authors/", views.AuthorListView.as_view(), name="authors"),
    path("author/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path("mybooks/", views.LoanedBooksByUserModelListView.as_view(), name="my-borrowed"),
    path("book/<slug:pk>/renew/", views.renew_book_librarian, name="renew-book-librarian"),
]
