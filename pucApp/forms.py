from django import forms
from django.core import validators

from . import models

class PUCCertificateForm(forms.ModelForm):
    class Meta:
        model=models.PUCCertificate
        fields='__all__'


class DownloadPUCForm(forms.Form):
    registration_number=forms.CharField(validators=
                              [validators.MinLengthValidator(10),
                               validators.MaxLengthValidator(10)])
    chasis_number=forms.CharField(validators=
                              [validators.MinLengthValidator(5),
                               validators.MaxLengthValidator(5)])