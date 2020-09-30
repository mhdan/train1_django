from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import permission_required, login_required
# this for permission required for specific func View
from django.contrib.auth.mixins import LoginRequiredMixin
# for required login to specific View!
import datetime

from . import models
from . import forms


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


class AuthorDetailView(generic.DetailView):
    model = models.Author
    template_name = "my_library/author_detail.html"


class LoanedBooksByUserModelListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user. 
    """
    model = models.BookInstance
    template_name = "my_library/bookinstance_list_borrowed_user.html"
    paginate_by = 10
    # this for count of instances show on each page!

    def get_queryset(self):
        return models.BookInstance.objects.filter(borrower=self.request.user
                                                  ).filter(status__exact='o').order_by('due_back')


# # it didn't work, and don't let user access this View even if they the specific access!
# @permission_required('mylibrary.can_renew_due_back')
def renew_book_librarian(request, pk):
    """
    View function for renewing a specific BookInstance by librarian
    """
    book_inst = get_object_or_404(models.BookInstance, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = forms.RenewBookForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_inst.due_back = form.cleaned_data['renewal_date']
            book_inst.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('my_library:my-borrowed'))

    # If this is a GET (or any other method) create the default form.
    # when the user don't send post method (e.g. for first time loading page)
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        form = forms.RenewBookForm(
            initial={'renewal_date': proposed_renewal_date})

    return render(request, 'my_library/book_renew_librarian.html', {'form': form, 'bookinst': book_inst})
