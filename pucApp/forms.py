from django import forms
from django.core import validators

from . import models

class PUCCertificateForm(forms.ModelForm):
    class Meta:
        model=models.PUCCertificate
        fields=['registration_number','chasis_number','contact_number','certificate']

    def clean_registration_number(self):
        inputed_registration_number=self.cleaned_data['registration_number']

        if len(inputed_registration_number)>10 or len(inputed_registration_number)<10:
                raise forms.ValidationError('should consists exactly 10 characters')
            
        return inputed_registration_number
        
    def clean_chasis_number(self):
        inputed_chasis_number=self.cleaned_data['chasis_number']

        if len(inputed_chasis_number)>5 or len(inputed_chasis_number)<5:
                raise forms.ValidationError('should consists exactly 10 characters')
            
        return inputed_chasis_number
        

    def clean_contact_number(self):
        inputed_contact_number=self.cleaned_data['contact_number']

        if len(inputed_contact_number)>10 or len(inputed_contact_number)<10:
                raise forms.ValidationError('should consists exactly 10 characters')
            
        return inputed_contact_number


class DownloadPUCForm(forms.Form):
    registration_number=forms.CharField(validators=
                              [validators.MinLengthValidator(10),
                               validators.MaxLengthValidator(10)])
    chasis_number=forms.CharField(validators=
                              [validators.MinLengthValidator(5),
                               validators.MaxLengthValidator(5)])