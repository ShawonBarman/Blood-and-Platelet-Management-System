from django.shortcuts import render, redirect
from . import models
from donor import models as dmodels
from .forms import RequestForm, UserContactsForm, RequestFormAnyone
from django.http import HttpResponseRedirect


def home_view(request):
    if request.method == 'POST':
        form = UserContactsForm(request.POST)
        if form.is_valid():
            form.save()
            dict = request.POST
            if dict['name'] == '':
                error_name = 'Name is required. Please Enter your name'
                return render(request, 'home.html', {'form': form, 'error_name': error_name})
            return redirect('home')

    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    form = UserContactsForm(request.POST)
    context = {
        'form': form
    }
    return render(request, 'index.html',context)

def is_donor(user):
    return user.groups.filter(name='DONOR').exists()

def is_patient(user):
    return user.groups.filter(name='PATIENT').exists()

def afterlogin_view(request):
    if is_donor(request.user):
        return redirect('donor-dashboard')

    elif is_patient(request.user):
        return redirect('patient-dashboard')

def available_donor(request):
    x = dmodels.Donor.objects.all()
    return render(request, 'available_donor.html', {'donors':x})

def about_us(request):
    return render(request, 'about.html')

def contact_us(request):
    return render(request, 'contact.html')

def search(request):
    if request.method == "POST":
        bloodGroup = request.POST.get('bloodgroup')
        donors = dmodels.Donor.objects.filter(bloodgroup=bloodGroup)
        print(donors)
        return render(request, "search.html", {"donors":donors})
    return render(request, "search.html")

def makeRequest(request, id):
    d = dmodels.Donor.objects.get(pk=id)
    print(d.id)
    request_form = RequestFormAnyone()
    if request.method == 'POST':
        request_form = RequestFormAnyone(request.POST)
        if request_form.is_valid():
            p_name = request_form.cleaned_data['patient_name']
            p_age = request_form.cleaned_data['patient_age']
            p_mobile = request_form.cleaned_data['patient_mobile']
            reason = request_form.cleaned_data['reason']
            bloodgroup = request_form.cleaned_data['bloodgroup']
            unit = request_form.cleaned_data['unit']
            hospital_name = request_form.cleaned_data['hospital_name']
            req_object = models.BloodRequestAnyone(donor_id = d.id,donor_name=d.user.first_name+" "+d.user.last_name,patient_name=p_name,patient_age=p_age,patient_mobile=p_mobile,reason=reason,bloodgroup=bloodgroup,unit=unit,hospital_name=hospital_name)
            req_object.save()
            print(d.id, d.user.first_name+" "+d.user.last_name, p_name,p_age,p_mobile,reason,bloodgroup,unit,hospital_name)
            return redirect('home')
    return render(request, "makeRequest.html", {'request_form':request_form, "donor":d})