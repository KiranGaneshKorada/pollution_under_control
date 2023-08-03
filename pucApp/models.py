from django.db import models
from django.core.validators import MinLengthValidator
import datetime

# Create your models here.

class PUCCertificate(models.Model):
    registration_number=models.CharField(max_length=10,primary_key=True)
    chasis_number=models.CharField(max_length=5)
    contact_number=models.CharField(max_length=10,validators=[MinLengthValidator(10,'enter a valid contact number')])
    date_uploaded=models.DateField(auto_now=True,null=True)
    certificate=models.FileField(upload_to='static/certificates')


class ContactUs(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField()

    def __str__(self):
        return self.name

