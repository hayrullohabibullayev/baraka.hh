from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class DebdBook(models.Model):
    full_name = models.CharField(max_length=180)
    ad_Date = models.DateTimeField(auto_now_add=True)
    borrowed = models.IntegerField()
    top_price = models.FloatField(max_length=520)
    return_date = models.DateField()
    def __str__(self):
        return self.full_name
    def tannarx(self):
        one = self.borrowed / 100
        two = one *  self.top_price
        there = self.borrowed - two
        return there
    def ustki_narx(self):
        one = self.borrowed / 100
        two = one *  self.top_price
        return two
    def obshi_pul(self):
        uzgaruvchi = self.borrowed
        return uzgaruvchi
    
class Abarots(models.Model):
    product_name = models.CharField(max_length=989)
    product_price = MoneyField(max_digits=27, decimal_places=1, default_currency='USD')
    number_product = models.IntegerField()
        
    def __str__(self):
        return self.product_name
    def obshi_mahsulot(self):
        delta = self.number_product
        return delta
    def product_total_price(self):
        one = self.number_product * self.product_price
        return one
         
class User_profil_Create(models.Model):
    username = models.OneToOneField(User, on_delete=CASCADE, blank=True)
    emeail_adress = models.EmailField()
    full_name = models.CharField(max_length=50)
    adress = models.CharField(max_length=80)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=9)
    abaut_me = models.TextField()
    avatar = models.ImageField(upload_to='profile', blank=True, null=True)
    
    def __str__(self):
        return str(self.username)
    def userusername(self):
        one = self.username
        return one
 
class Zakaz(models.Model):
    zakaz_nomi = models.CharField(max_length=550)
    zakaz_soni = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.zakaz_nomi
    def buyurtmasoni(self):
        one = self.zakaz_soni
        return one
  
class Habar(models.Model):
    write_message = models.CharField(max_length=1000000)
    added_date = models.TimeField(auto_now_add=True)
    
    def __str__(self):
        return self.write_message
    


