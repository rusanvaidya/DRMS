from email.policy import default
from django.db import models

# Create your models here.

class medicalreport(models.Model):
    id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=60, default=None)
    hospital_name = models.CharField(max_length=60, default=None)
    doctor_name = models.CharField(max_length=60, default=None)
    report_of = models.CharField(max_length=60, default=None)
    specifed_problem = models.CharField(max_length=60, default=None)
    report_file = models.ImageField(upload_to='Patient', default=None)