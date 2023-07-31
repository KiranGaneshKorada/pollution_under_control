from django.db import models
from django.core.validators import MinLengthValidator
from datetime import date
from django.utils import timezone

# Create your models here.

class PUCCertificate(models.Model):
    registration_number=models.CharField(max_length=10,primary_key=True)
    chasis_number=models.CharField(max_length=5)
    contact_number=models.CharField(max_length=10,validators=[MinLengthValidator(10,'enter a valid contact number')])
    date_uploaded=models.DateTimeField(auto_now_add=True)
    certificate=models.FileField(upload_to='static/certificates')

