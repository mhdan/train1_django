from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.db.models import F
from . import models


# def index(request):
#     """
#     index view for first page of polls!
#     """
#     latest_question_list = models.Question.objects.order_by('-pub_date')
#     context = {'latest_q_list': latest_question_list}
#     return render(request, 'polls/index.html', context)
#
class IndexListView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_q_list'

    def get_queryset(self):
        """Return the last 5 published questions."""
        return models.Question.objects.order_by('-pub_date')[:5]


# def detail(request, question_id):
#     """
#     detail view for each question.
#     """
#     question = get_object_or_404(models.Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'q': question})
#
class QuestionDetailView(generic.DetailView):
    model = models.Question
    template_name = "polls/detail.html"


# def results(request, question_id):
#     """
#     results view for each question.
#     """
#     question = get_object_or_404(models.Question, pk=question_id)
#     return render(request, 'polls/result.html', {'q': question})
#
class ResultDetailView(generic.DetailView):
    model = models.Question
    template_name = "polls/result.html"


def vote(request, question_id):
    """
    vote view for each question.
    """
    question = get_object_or_404(models.Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, models.Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:
        selected_choice.vote = F('vote') + 1
        selected_choice.save()
        # we can use above code for avoiding race condition with 'F()' function!!!
        # selected_choice.vote += 1
        # selected_choice.save()
        
        # # Always return an HttpResponseRedirect after successfully dealing
        # # with POST data. This prevents data from being posted twice if a
        # # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=[question_id]))
