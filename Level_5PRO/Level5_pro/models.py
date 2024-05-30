from django.db import models
from django.contrib.auth.models import User # import the user bulid in model

class userdetail(models.Model):
    
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    pot_url=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True) # profile pics is the folder in side the media folder
    def __str__(self):
        return self.user.username

# Create your models here.
