from django.urls import path
from . import views


# set the 'app_name' to namespaceing in urls!!!
app_name = 'my_library'
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
]
