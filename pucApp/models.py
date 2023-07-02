from django.db import models

# Create your models here.

class PUCCertificate(models.Model):
    registration_number=models.CharField(max_length=10,primary_key=True)
    chasis_number=models.CharField(max_length=5)
    certificate=models.FileField(upload_to='static/certificates')

