from django.shortcuts import render,HttpResponse
from django.forms.models import model_to_dict
from django.views.generic import View
from .forms import PUCCertificateForm,DownloadPUCForm
from .models import PUCCertificate

# Create your views here.

def uploadPUC(request):
    form=PUCCertificateForm()
    if request.method=='POST':
        puc_certificate=PUCCertificateForm(request.POST,request.FILES)
        if puc_certificate.is_valid():
            puc_certificate.save()
            return HttpResponse("dddfdfdfd")
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
                response=HttpResponse(certificate.certificate,content_type='application/pdf')
                #response['Content-Disposition']=f'attachment;filename="{certificate.certificate.name+certificate.registration_number}"'
                return response
            
        return render(request,'pucApp/downloadPUC',{'form':DownloadPUCForm(),'errorMsg':'invalid credintials'})
