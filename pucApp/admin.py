from django.contrib import admin
from . import models

# Register your models here.
class PucCertificateAdmin(admin.ModelAdmin):
    readonly_fields=('date_uploaded',)
admin.site.register(models.PUCCertificate,PucCertificateAdmin)


admin.site.register(models.ContactUs)
