from django.urls import path
from . import views
app_name="polls"
urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('', views.register, name="register"),
    path('Fruits/Dragon-west.html', views.Dragon_west, name='Dragon_west'),
]