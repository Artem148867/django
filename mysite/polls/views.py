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
        user = TestUser(email=email, password=password)
        user.save()
        
        return render(request, 'index.html')
    except Exception as e:
        return render(request, "Register/forma.html")

    