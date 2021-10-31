from django.shortcuts import render, redirect
from . import forms, models
from django.contrib.auth.models import Group
from django.contrib.auth import get_user
from django.http import HttpResponseRedirect
from blood import forms as bforms
from blood import models as bmodels

def donor_signup_view(request):
    userForm = forms.DonorUserForm()
    donorForm = forms.DonorForm()
    mydict = {'userForm':userForm, 'donorForm':donorForm}

    if request.method == 'POST':
        userForm = forms.DonorUserForm(request.POST)
        donorForm = forms.DonorForm(request.POST,request.FILES)
        if userForm.is_valid() and donorForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            donor = donorForm.save(commit=False)
            donor.user = user
            donor.bloodgroup = donorForm.cleaned_data['bloodgroup']
            donor.save()
            my_donor_group = Group.objects.get_or_create(name='DONOR')
            my_donor_group[0].user_set.add(user)
        return HttpResponseRedirect('donorlogin')

    return render(request, 'donor/donorsignup.html', context=mydict)


def donor_dashboard_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    dict={
        'requestpending': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(status='Pending').count(),
        'requestapproved': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(status='Approved').count(),
        'requestmade': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).count(),
        'requestrejected': bmodels.BloodRequest.objects.all().filter(request_by_donor=donor).filter(status='Rejected').count(),
    }
    return render(request, 'donor/donor_dashboard.html', context=dict)


def donate_blood_view(request):
    donation_form = forms.DonationForm()

    if request.method=='POST':
        donation_form = forms.DonationForm(request.POST)
        if donation_form.is_valid():
            blood_donate = donation_form.save(commit=False)
            blood_donate.bloodgroup = donation_form.cleaned_data['bloodgroup']
            donor = models.Donor.objects.get(user_id=request.user.id)
            blood_donate.donor = donor
            blood_donate.save()
            return HttpResponseRedirect('donation-history')
    return render(request,'donor/donate_blood.html',{'donation_form':donation_form})

def donation_history_view(request):
    donor = models.Donor.objects.get(user_id=request.user.id)
    donations = models.BloodDonate.objects.all().filter(donor=donor)
    return render(request,'donor/donation_history.html', {'donations':donations})

def make_request_view(request):
    request_form = bforms.RequestForm()
    if request.method == 'POST':
        request_form = bforms.RequestForm(request.POST)
        if request_form.is_valid():
            blood_request = request_form.save(commit=False)
            blood_request.bloodgroup = request_form.cleaned_data['bloodgroup']
            donor = models.Donor.objects.get(user_id=request.user.id)
            blood_request.request_by_donor = donor
            blood_request.save()
            return HttpResponseRedirect('request-history')
    return render(request, 'donor/makerequest.html', {'request_form':request_form})

def request_history_view(request):
    donor = models.Donor.objects.get(user_id = request.user.id)
    blood_request = bmodels.BloodRequest.objects.all().filter(request_by_donor = donor)
    return render(request, 'donor/request_history.html', {'blood_request':blood_request})

def patient_requested(request, id):
    x = bmodels.BloodRequest.objects.all()
    current_user = get_user(request)
    # print(current_user.username)
    donor = models.Donor.objects.get(user_id=current_user)
    # print(donor.id)
    # print(donor.bloodgroup)
    arr = []
    for i in x:
        if donor.bloodgroup == i.bloodgroup:
            print(i.id)
            arr.append(i)
    # print(arr)
    if request.method == "POST":
        approved = request.POST.get('approved')
        rejected = request.POST.get('rejected')
        # print(approved)
        # print(rejected)
        if approved != None:
            bloodrequest = bmodels.BloodRequest.objects.get(pk=id)
            # print(bloodrequest.patient_name)
            bloodrequest.status = "Approved"
            bloodrequest.save()
            return redirect("donor-dashboard")
        elif rejected != None:
            bloodrequest = bmodels.BloodRequest.objects.get(pk=id)
            # print(bloodrequest.patient_name)
            bloodrequest.status = "Rejected"
            bloodrequest.save()
            return redirect("donor-dashboard")
    return render(request, "donor/patient_requested.html", {"details":arr})

def d_profile(request):
    user = get_user(request)
    donor = models.Donor.objects.get(user_id=user)
    context={
        'name': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'blood_group' : donor.bloodgroup,
        'phone_number': donor.mobile,
        'address' : donor.address,
        'donor':donor
    }
    return render(request, 'donor/donor_profile.html',context)