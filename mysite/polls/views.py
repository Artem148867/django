from django.http import HttpResponse, HttpResponseRedirect

from .models import Client, Product, Role
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    cards = Product.objects.all()
    print(cards)
    return render(request, 'index.html', {'products': cards})

def Dragon_east(request):
   return render(request, 'Fruits/Dragon-east.html')

def Dragon_west(request):
   return render(request, 'Fruits/Dragon-west.html')

def Kitsune(request):
   return render(request, 'Fruits/kitsune.html')

def Yeti(request):
   return render(request, 'Fruits/Yeti.html')

def Leopard(request):
   return render(request, 'Fruits/Leopard.html')

def Gravity(request):
   return render(request, 'Fruits/Gravity.html')      

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
        if Client.objects.filter(email=email).exists():
            context["error"] = "Пользователь с таким email уже существует"
            return render(request, 'Register/forma.html', context)
        else:
            role = Role.objects.get(id=1)
            user = Client(email=email, password=password, login=login, role=role)
            user.save()
            return index(request)
        
    except Exception as e:
        return render(request, "Register/forma.html")
@csrf_exempt
def join(request):
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('pass')
        
        try:    
            client = Client.objects.get(email=username)
            if client.password == password:
                request.session['user_id'] = client.id
                return index(request)

            else:
                return render(request, 'Register/join.html', {'error': 'Неверный пароль.'})
        
        except Client.DoesNotExist:
            return render(request, 'Register/join.html', {'error': 'Пользователь не найден.'})

    return render(request, 'Register/join.html')