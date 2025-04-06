from django.urls import path
from . import views
app_name="polls"
urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    path('<int:question_id>/vote', views.votes, name="vote"),
    path('', views.register, name="register")
]