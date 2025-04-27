from django.http import HttpResponse, HttpResponseRedirect

from .models import TestUser
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def index(request):
   return render(request, 'index.html')

def Dragon_west(request):
   return render(request, 'Fruits/Dragon-west.html')

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
        login = request.POST['login']
        context = dict()
        if TestUser.objects.filter(email=email).exists():
            context["error"] = "Пользователь с таким email уже существует"
            return render(request, 'Register/forma.html', context)
        else:
            user = TestUser(email=email, password=password, login=login)
            user.save()
            return render(request, 'index.html',)
        
    except Exception as e:
        return render(request, "Register/forma.html")
@csrf_exempt
def join(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pass')
        
        try:
            client = TestUser.objects.get(email=username)
            if client.password == password:
                request.session['user_id'] = client.id
                return render(request, "index.html")

            else:
                return render(request, 'Register/join.html', {'error': 'Неверный пароль.'})
        
        except TestUser.DoesNotExist:
            return render(request, 'Register/join.html', {'error': 'Пользователь не найден.'})

    return render(request, 'Register/join.html')