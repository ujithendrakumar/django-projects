from django.db import models

class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250)
    age = models.CharField(max_length=150)
    school = models.ForeignKey(School,related_name='students',on_delete=None)
    def __str__(self):
        return self.name
