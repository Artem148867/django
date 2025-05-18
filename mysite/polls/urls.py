from django.urls import path
from . import views
app_name="polls"
urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('', views.register, name="register"),
    path('Fruits/Dragon-west.html', views.Dragon_west, name='Dragon_west'),
    path('Fruits/Dragon-east.html', views.Dragon_east, name='Dragon_east'),
    path('Fruits/Kitsune.html', views.Kitsune, name='Kitsune'),
    path('Fruits/Yeti.html', views.Yeti, name='Yeti'),
    path('Fruits/Leopard.html', views.Leopard, name='Leopard'),
    path('Fruits/Gravity.html', views.Gravity, name='Gravity'),
    path('auth', views.join, name='auth'),
    path('main', views.index, name='index'),
]