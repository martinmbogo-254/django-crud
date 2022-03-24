from django.db import models
from django.urls import reverse

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

class Item(models.Model):
    name = models.CharField(max_length=100)
    item_type = models.CharField(max_length=250)
    acquisition_cost = models.IntegerField(max_length=100)
    source =models.CharField(max_length=100)
    item_properties = models.TextField(max_length=250)
    listing_platform = models.CharField(max_length=100)
    Date =models.DateTimeField()
    listing_price = models.IntegerField(max_length=100)
    date_of_sale = models.DateTimeField()
    sale_price = models.IntegerField(max_length=100)
    item_image = models.FileField(upload_to='images/',default='images/default.jpg')

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = ("department")
        verbose_name_plural = ("departments")

    def __str__(self):
        return self.name

   
class kaspersky(models.Model):
    unid = models.TextField(max_length=100)

    def __str__(self):
        return self.unid

class Antivirus(models.Model):
    kaspersky = models.ForeignKey(kaspersky,on_delete=models.CASCADE)
    officer_name = models.CharField(max_length=250)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    directorate = models.CharField(max_length=250)
    comp_serial_no =models.CharField(max_length=250)

    class Meta:
        verbose_name = ("antivirus")
        verbose_name_plural = ("antiviruses")

    def __str__(self):
        return self.kaspersky

    def get_absolute_url(self):
        return reverse("antivirus_list", kwargs={"pk": self.pk})





