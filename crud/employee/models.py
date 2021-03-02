from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=25,null=False,default='admin')

    def __str__(self):
        return self.title


class Employee(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=20, default='enter your email address')
    mobile = models.CharField(max_length=14)
    emp_code = models.CharField(max_length=50)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.name





