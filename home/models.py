from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now = True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    zipcode = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(null = True, blank = True, upload_to = 'static/images/')

    def __str__(self):
        return self.user.username
    
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)
        user_profile.save()
post_save.connect(create_profile, sender = User)

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
        
# Create your models here.
class Donate(models.Model):
    name= models.CharField(max_length=120)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=20)
    desc= models.TextField()
    date= models.DateField()
    def __str__(self):
        return self.name

class Reports(models.Model):
    user= models.CharField("User Name", max_length=50)
    Pregnancies= models.FloatField(null=True, blank=True)
    Glucose=models.FloatField(null=True, blank=True)
    Blood_Pressure=models.FloatField(null=True, blank=True)
    Skin_Thickness=models.FloatField(null=True, blank=True)
    Insulin=models.FloatField(null=True, blank=True)
    BMI=models.FloatField(null=True, blank=True)
    D_P_Function=models.FloatField(null=True, blank=True)
    Age=models.FloatField(null=True, blank=True)
    Result=models.TextField(max_length=30)
    def __str__(self):
        return self.user
  
  
