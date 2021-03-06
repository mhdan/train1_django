from django.db import models
import uuid  # Required for unique book instances
from django.urls import reverse
# Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
# user with authenticating ability
from datetime import date


class Author(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)

    # this is specific func for django that we override, return to specifc part on site.(maybe specific view)
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('my_library:author-detail', args=[str(self.id)])


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    # 'Book' as a string rather than object because it hasn't been declared yet in the file.
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Mainstance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS,
                              blank=True, default='m', help_text='Book availability')
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL,
                                 null=True, blank=True)

    # the 'Meta' class is used for ordering the items of class in queries!
    # we set the fields that we want to sort based on in ordering list!!!
    class Meta:
        ordering = ["due_back"]
        # we can also set that null values were on the last!!!!
        permissions = [('can_renew_due_back', 'Can renew due back')]
        # set permission access!

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id, self.book.title)

    # property make it available same as filed :)
    # @property
    def _is_overdue(self):
        """
        if the due_back is over and been late return True
        else if have time return True
        """
        if self.due_back and (date.today() > self.due_back):
            return True
        return False
    # show icon instead of 'True' or 'False'
    _is_overdue.boolean = True
    _is_overdue.short_description = 'overdue for back?'
    _is_overdue.admin_order_field = 'due_back'
    # make property of func in other attribute
    is_overdue = property(_is_overdue)


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000,
                               help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN', max_length=13,
                            help_text="13 Character <a href=https://www.isbn-international.org/content/what-isbn>ISBN number</a>")
    # as we can see here, we can ues html tags in help_text
    genre = models.ManyToManyField('Genre',
                                   help_text="Select a genre for this book")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title

    # this is specific func for django that we override, return to specifc part on site.(maybe specific view)
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('my_library:book-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        # query self.genre.all() and then access to name using genre.name for 3 of them!
        return ', '.join([genre.name for genre in self.genre.all()[:3]])
    # this is the title of column in list_display on admin panel!!!
    display_genre.short_description = 'Genre'


class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200,
                            help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
