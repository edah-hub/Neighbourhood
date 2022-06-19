from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField


# Create your models here.
class User(AbstractUser):
   email = models.EmailField(unique=True)
   bio = models.TextField(null=True)
   neighboorhood = models.CharField(max_length=100, null=True)
   image = CloudinaryField('image', null=True, blank=True, default='image/upload/v1654285390/hz7a08c74kynhnx24lwd.png')
   contact = models.CharField(max_length=100 ,blank=True, null=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username']
   
   
class NeighbourHood(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
      ordering = ['-created']
    def __str__(self):
        return self.name
     
class Business(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    body = models.TextField(null=True)
    contact = models.CharField(max_length=200)
    neighbourHood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
      ordering = ['-created']
    def __str__(self):
        return self.name
     
     
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighbourHood = models.ForeignKey(NeighbourHood, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
      ordering = ['-created']
    def __str__(self):
        return self.body