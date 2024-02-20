from django.db import models
from django.contrib.auth.models import User
import datetime
from django.core.validators import MinValueValidator

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    date_of_joining = models.DateField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('inactive', 'Inactive')])

    def __str__(self):
         return f"{self.first_name}  {self.last_name}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    price = models.PositiveIntegerField()
    entered_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialisation = models.CharField(max_length=100)
    contact = models.IntegerField()
    location = models.CharField(max_length=100)
    entered_by = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)  
    date = models.DateField(default=datetime.date.today)
    time = models.TimeField(default=datetime.time)  
    entered_by = models.ForeignKey(Employee, on_delete=models.CASCADE)  

    def __str__(self):
        return f"{self.doctor} - {self.date} - {self.time}" 
        


class DealsDetail(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField(default=1)
    entered_by = models.ForeignKey(Employee, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Doctor: {self.doctor}, Product: {self.product}, entered_by: {self.entered_by}"

    

    # username:- admin
    # password :- admin@2903
