from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Class(models.Model):
    classname = models.CharField(max_length=200, null=True, blank=True)
    image = models.FileField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    cost = models.CharField(max_length=200, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.classname

class Registration(models.Model):
    classname = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    registernumber = models.CharField(max_length=200, null=True, blank=True)
    message = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=100, default='New', null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def totalprice1(self):
        return (self.classname.cost) * int(self.registernumber)

class Teacher(models.Model):
    classname = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
    teachername = models.CharField(max_length=200, null=True, blank=True)
    teacherimage = models.FileField(max_length=200, null=True, blank=True)
    mobile = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)
    creationdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teachername

class About(models.Model):
    pagetitle = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.pagetitle

class Contact(models.Model):
    pagetitle = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    timing = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.pagetitle

class Invoice(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    payment = models.CharField(max_length=200, null=True, blank=True)
    paymentmode = models.CharField(max_length=200, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment

class Trackinghistory(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE, null=True, blank=True)
    remark = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.remark
