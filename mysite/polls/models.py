from django.db import models
from django.contrib import admin

class TestUser(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    login = models.CharField(max_length=200)

class Role(models.Model):
    role_name = models.CharField(max_length=10)

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_login = models.CharField(max_length=50)
    role = models.ForeignKey(Role, on_delete = models.CASCADE)

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')

class Product(models.Model):
    product_id = models.CharField(max_length=40)
    product_name = models.CharField(max_length=40)
    price = models.IntegerField(default=99)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

class Followed(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

admin.site.register(TestUser)
admin.site.register(Role)
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Product)
admin.site.register(Followed)