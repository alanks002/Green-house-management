from django.db import models

# Create your models here.

class singledb(models.Model):
    Title=models.CharField(max_length=30,null=True,blank=True)
    Profile = models.ImageField(upload_to="img", null=True, blank=True)
    Icon=models.CharField(max_length=30,null=True,blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)




class State(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

