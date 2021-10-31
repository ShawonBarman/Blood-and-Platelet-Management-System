from django import forms

from . import models

class UserContactsForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['name',
                  'email',
                  'message',
                 ]

class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodRequest
        fields=['patient_name','patient_age','reason','bloodgroup','unit','hospital_name']

class RequestFormAnyone(forms.ModelForm):
    class Meta:
        model=models.BloodRequestAnyone
        fields=['patient_name','patient_age', 'patient_mobile', 'reason','bloodgroup','unit','hospital_name']