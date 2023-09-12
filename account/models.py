from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Packages(models.Model):
    packagename=models.CharField(max_length=200)
    price= models.IntegerField()
    image=models.ImageField(upload_to='package_images')
    image2=models.ImageField(upload_to='package_images',default='default_image.jpg')
    image3=models.ImageField(upload_to='package_images',default='default_image.jpg')
    description=models.CharField(max_length=1000)
    days=models.IntegerField()
    location=models.CharField(max_length=100)
    pickingdeparture=models.CharField(max_length=300)
    chekingtime=models.TimeField()
    hotelname=models.CharField(max_length=300)
    
   
    returnairporttime=models.TimeField()
    pickoutdeparture=models.CharField(max_length=300)
    checkouttime=models.TimeField()
    upcoming=models.BooleanField(default=True)


class TravelItinerary(models.Model):
    day = models.IntegerField()  # Day number
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name="iteneries")
    activities = models.JSONField()  # JSONField to store a list of activities

    def __str__(self):
        return f"Day {self.day} - Itinerary"
    

class Event(models.Model):
    eventname=models.CharField(max_length=300)
    package = models.ForeignKey(Packages, on_delete=models.CASCADE, related_name="events")
    date=models.DateField(null=True)
    


class Intrested(models.Model):
    date=models.DateField()
    package=models.ForeignKey(Packages,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    memberes=models.IntegerField()
    message=models.CharField(max_length=500, null=True)
    name=models.CharField(max_length=100, null=True)
    phone=models.IntegerField(null=True)    
    email=models.EmailField(null=True)    

    @property
    def totalamt(self):
        return self.package.price*self.memberes
    


class Mytrip (models.Model):
    intrested=models.OneToOneField(Intrested,on_delete=models.CASCADE,related_name="intrestedpackage")
    dete=models.DateField(auto_now_add=True)



class Booked(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=True)

    package=models.ForeignKey(Packages,on_delete=models.CASCADE,related_name="intbooked")
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=500,null=True)
    phone=models.IntegerField(null=True)



