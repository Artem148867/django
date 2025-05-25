from django.db import models
from django.contrib import admin

class Role(models.Model):
    role_name = models.CharField(max_length=10)

class Client(models.Model):
    email = models.CharField(max_length=200, unique=True, default='')
    password = models.CharField(max_length=200, default='')
    login = models.CharField(max_length=200, default='')
    role = models.ForeignKey(Role, on_delete = models.CASCADE)

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='received_messages')

class Product(models.Model):
    product_id = models.CharField(max_length=40)
    product_name = models.CharField(max_length=40)
    product_price = models.IntegerField(default=1)
    product_owner = models.ForeignKey(Client, on_delete = models.CASCADE)
    product_discount = models.IntegerField(default=0)
    product_image = models.CharField(max_length=100, default='')
    product_url = models.TextField(default='')

class Followed(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    user_id = models.ForeignKey(Client, on_delete = models.CASCADE)

admin.site.register(Client)
admin.site.register(Role)
admin.site.register(Message)
admin.site.register(Product)
admin.site.register(Followed)