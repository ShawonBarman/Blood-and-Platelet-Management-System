from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="Login To BPMS"
admin.site.site_title="Dashboard"
admin.site.index_title="Welcome To This Dashboard"

admin.site.register(Contact)
admin.site.register(Stock)
admin.site.register(BloodRequest)
admin.site.register(BloodRequestAnyone)