from django.db import models
from django.contrib import admin

class Role(models.Model):
    role_name = models.CharField(maxlength=10)

class User(models.Model):
    user_name = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_login = models.CharField(max_length=50)
    user_id = models.ForeignKey(Role, on_delete = models.CASCADE)

class Message(models.Model):
    message_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    sender = models.ForeignKey(User, on_delete = models.CASCADE)

class Product(models.Model):
    product_id = models.CharField(max_length=40)
    product_name = models.CharField(max_length=40)
    price = models.integerField(default=99)
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

class Folowed(models.Model):
    product_id = models.ForeignKey(Product, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

admin.site.register(Role)
admin.site.register(User)
admin.site.register(Message)
admin.site.register(Product)
admin.site.register(Folowed)