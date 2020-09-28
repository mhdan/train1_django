from django.urls import path, re_path   # 're_path' is alias for 'url'
from . import views


# set the 'app_name' to namespaceing in urls!!!
app_name = 'polls'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path("<int:pk>/", views.QuestionDetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultDetailView.as_view(), name="results"),
    # we should ues re_path for particular regex and for common ones should use <int:pk>, <str:pk> !!!
    # here is expample for re_path:
    # re_path(r"^(?P<pk>[0-9]+)/$", views.QuestionDetailView.as_view(), name="detail"),
    re_path(r"^(?P<question_id>[0-9]+)/vote/$", views.vote, name="vote"),
    



    # # or we can use re_path() to use regex and sending params in urls!!!!
    # re_path(r"^$", views.index, name="index"),
]
