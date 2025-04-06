from django.http import HttpResponse, HttpResponseRedirect

from .models import TestUser
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def index(request):
   return render(request, 'index.html')

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
    context = {'users': []}
    return render(request, 'Register/forma.html', context)

@csrf_exempt
def register(request):
    try:
        email = request.POST['email']
        password = request.POST['pass']
        user = TestUser(email=email, password=password)
        user.save()
    except:
        pass

    list_users = TestUser.objects.all()
    context = {'users': list_users}
    return render(request, 'Register/forma.html', context)