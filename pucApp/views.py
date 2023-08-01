from django.shortcuts import render,HttpResponse
from django.forms.models import model_to_dict
from django.views.generic import View
from .forms import PUCCertificateForm,DownloadPUCForm
from .models import PUCCertificate
from django.contrib.auth.decorators import login_required
import datetime
from . import smsapi
import pywhatkit


# Create your views here.

def home(request):
    return render(request,'pucApp/home.html')

@login_required
def uploadPUC(request):
    form=PUCCertificateForm()
    if request.method=='POST':
        puc_certificate=PUCCertificateForm(request.POST,request.FILES)
        #puc_certificate.cleaned_data['date_uploaded']=datetime.date.today
        print(puc_certificate)
        if puc_certificate.is_valid():
            puc_certificate.save()
    return render(request,'pucApp/uploadPUC.html',{'form':form})


class downloadPUC(View):

    def get(self,request):
        return render(request,'pucApp/downloadPUC.html',{'form':DownloadPUCForm()})
    
    def post(self,request):
        form=DownloadPUCForm(request.POST)
        if form.is_valid():
            rno=form.cleaned_data['registration_number']
            if PUCCertificate.objects.filter(registration_number=rno):
                certificate=PUCCertificate.objects.get(registration_number=rno)
                print(model_to_dict(certificate))
                cert=certificate
                print(cert.date_uploaded)
                response=HttpResponse(certificate.certificate,content_type='application/pdf')
                #response['Content-Disposition']=f'attachment;filename="{certificate.certificate.name+certificate.registration_number}"'
                return response
            
        return render(request,'pucApp/downloadPUC',{'form':DownloadPUCForm(),'errorMsg':'invalid credintials'})

def remainder(request):
    data=PUCCertificate.objects.all()
    for a in data:
        print(a)
        diff=datetime.date.today()-a.date_uploaded
        print(diff.days)
        dif=diff.days
        if dif>=0:
            #smsapi.sendMessage(a.contact_number)
            pywhatkit.sendwhatmsg('+919573385356','Kindly renew your Pollution under Control certificate',(datetime.datetime.now().hour),(datetime.datetime.now().minute)+1)
    return render(request,'pucApp/home.html')