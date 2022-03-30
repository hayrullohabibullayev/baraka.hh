from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active']

class UserprofileCreate(forms.ModelForm):
    class Meta:
        model = User_profil_Create
        fields = ['username', 'emeail_adress', 'full_name', 'adress', 'city', 'country', 'postal_code', 'abaut_me']

class Create_Debt(forms.ModelForm):
    class Meta:
        model = DebdBook
        fields = ['full_name', 'borrowed', 'top_price', 'return_date']

class Create_buyurtmalar(forms.ModelForm):
    class Meta:
        model = Zakaz
        fields = ['zakaz_nomi', 'zakaz_soni']

class Create_abarot(forms.ModelForm):
    class Meta:
        model = Abarots
        fields = '__all__'
        
class Create_messages(forms.ModelForm):
    class Meta:
        model = Habar 
        fields = '__all__'       