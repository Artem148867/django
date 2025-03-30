from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404,render
from django.urls import reverse

def index(request):
   list_question = Question.objects.all()
   context = {'list':list_question}
   return render(request, 'index.html', context)

def votes(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question.id,)))
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "Ничего не выбрано!",
            })
def feedback(request):
    email = request.POST['email']
    print(f'\n\nClient email: {email}')