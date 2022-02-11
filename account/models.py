from email.policy import default
from django.db import models


class info_patient(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, blank=False)
    citizen_no = models.IntegerField(blank=False)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)

class info_doctor(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, blank=False)
    license_no = models.ImageField(upload_to="license")
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    field = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

class info_hospital(models.Model):
    id = models.AutoField(primary_key=True)
    hospital_name = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50)
    hospitalpan=models.IntegerField()
    email = models.CharField(max_length=50)


