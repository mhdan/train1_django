from django.shortcuts import render
from django.views import generic

from . import models


# def index(request):
#     """
#     View function for home page of site.
#     """
#     # Generate counts of some of the main objects
#     num_books = models.Book.objects.all().count()
#     num_instances = models.BookInstance.objects.all().count()
#     # Available books (status = 'a')
#     num_instances_available = models.BookInstance.objects.filter(status__exact='a'
#                                                                  ).count()
#     # The 'all()' is implied by default.
#     num_authors = models.Author.objects.all().count()
#
#     # Render the HTML template index.html with the data in the context variable
#     return render(request, 'my_library/index.html',
#                   context={'num_books': num_books, 'num_instances': num_instances,
#                            'num_instances_available': num_instances_available, 'num_authors': num_authors})
#
class IndexView(generic.TemplateView):
    template_name = "my_library/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_books"] = models.Book.objects.all().count()
        context["num_instances"] = models.BookInstance.objects.all().count()
        context["num_instances_available"] = models.BookInstance.objects.filter(
            status__exact='a').count()
        context["num_authors"] = models.Author.objects.all().count()
        return context


class BookListView(generic.ListView):
    model = models.Book
    template_name = "my_library/book_list.html"


class BookDetailView(generic.DetailView):
    model = models.Book
    template_name = "my_library/book_detail.html"


class AuthorListView(generic.ListView):
    model = models.Author
    template_name = "my_library/author_list.html"
