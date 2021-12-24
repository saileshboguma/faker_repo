from django.db import models


# Create your models here.
class Hydjob(models.Model):
    date = models.DateField();
    company = models.CharField(max_length=30);
    title = models.CharField(max_length=100);
    eligibility = models.CharField(max_length=100);
    address = models.CharField(max_length=100);
    email = models.EmailField();
    phonenumber = models.IntegerField();


class Bangalorejob(models.Model):
    date = models.DateField();
    company = models.CharField(max_length=30);
    title = models.CharField(max_length=100);
    eligibility = models.CharField(max_length=100);
    address = models.CharField(max_length=100);
    email = models.EmailField();
    phonenumber = models.IntegerField();


class Chennaijob(models.Model):
    date = models.DateField();
    company = models.CharField(max_length=30);
    title = models.CharField(max_length=100);
    eligibility = models.CharField(max_length=100);
    address = models.CharField(max_length=100);
    email = models.EmailField();
    phonenumber = models.IntegerField();


class Punejob(models.Model):
    date = models.DateField();
    company = models.CharField(max_length=30);
    title = models.CharField(max_length=100);
    eligibility = models.CharField(max_length=100);
    address = models.CharField(max_length=100);
    email = models.EmailField();
    phonenumber = models.IntegerField();
