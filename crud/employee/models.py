from django.db import models

# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=25,null=False,default='admin')

    def __str__(self):
        return self.title


class Employee(models.Model):
    Gender = [
        ('F', 'Female'),
        ('M','Male'),
    ]
    gender = models.CharField(max_length=2, choices=Gender, null=True,)
    name = models.CharField(max_length=25, null = True)
    email = models.EmailField(max_length=50, null = True)
    mobile = models.CharField(max_length=14, null = True)
    emp_code = models.CharField(max_length=50, null = True)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)

    def __str__(self):
        return self.name





