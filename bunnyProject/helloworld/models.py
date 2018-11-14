from django.db import models

# Create your models here.
class Name(models.Model):
    name= models.CharField(max_length=50)
    description =  models.TextField()
    publish = models.BooleanField(default=True) 

    def __str__(self):
        return self.name 

class UserTable(models.Model):
    name= models.CharField(max_length=50)
    mobile= models.CharField(max_length=12)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name 
    
  
