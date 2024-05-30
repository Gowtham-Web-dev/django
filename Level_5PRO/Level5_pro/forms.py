from django import forms
from django.contrib.auth.models import User
from Level5_pro.models import userdetail

class userDetailinfo(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')
class PrfileINfo(forms.ModelForm):
     class Meta():
         model=userdetail
         fields=('profile_pic','pot_url')