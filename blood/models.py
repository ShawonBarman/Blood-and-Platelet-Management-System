from django.db import models
from patient import models as pmodels
from donor import models as dmodels


class Stock(models.Model):
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.bloodgroup


class BloodRequest(models.Model):
    request_by_patient = models.ForeignKey(pmodels.Patient, null=True, on_delete=models.CASCADE)
    request_by_donor = models.ForeignKey(dmodels.Donor, null=True, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    reason = models.CharField(max_length=500)
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    hospital_name = models.CharField(max_length=50, default=None)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.bloodgroup

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.CharField(max_length=300)

class BloodRequestAnyone(models.Model):
    donor_id = models.IntegerField(null=True)
    donor_name = models.CharField(max_length=50, null=True)
    patient_name = models.CharField(max_length=30)
    patient_age = models.PositiveIntegerField()
    patient_mobile = models.CharField(max_length=20, null=True)
    reason = models.CharField(max_length=500)
    bloodgroup = models.CharField(max_length=10)
    unit = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, default="Pending")
    hospital_name = models.CharField(max_length=50, default=None)
    date = models.DateField(auto_now=True)