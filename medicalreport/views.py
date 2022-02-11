from django.shortcuts import render, redirect
from account.models import info_patient, info_doctor, info_hospital
from medicalreport.models import medicalreport
import os

def medicalrep(request):
    email = request.session['email']
    patient = info_patient.objects.filter(email=email)
    doctor = info_doctor.objects.filter(email=email)
    hospital = info_hospital.objects.filter(email=email)

    if patient.exists():
        try:
            if request.method == 'POST':
                pin = request.POST['pin']
                user_patient = info_patient.objects.filter(email=email, pin=pin)

                if user_patient.exists():
                    request.session['pin'] = pin
                    return render(request, 'medical_report.html', {'email': email, 'user_as': 'patient' ,'pin':pin})
                else:                
                    return redirect("/")

            if 'pin' in request.session:
                user_patient = info_patient.objects.filter(email=email, pin=request.session['pin'])
                pname = user_patient.values('full_name')[0]['full_name']
                patient_history = medicalreport.objects.filter(pname=pname)
                print(pname)
                if user_patient.exists():
                    return render(request, 'medical_report.html', {'email': email, 'user_as': 'patient', 'pin':request.session['pin'], 'patient_history': patient_history})
        except:
            return render(request, 'index.html', {'email': email})
        return redirect("/")
    
    if doctor.exists():
        return render(request, 'medical_report.html', {'email': email, 'user_as': 'doctor'})

    
    if hospital.exists():
        return render(request, 'medical_report.html', {'email': email, 'user_as': 'hospital'})

def new_mrecord(request): 
    if request.method == 'POST':
        email = request.session['email']
        patient = info_patient.objects.filter(email=email)
        pname = patient.values('full_name')
        hospital = request.POST['hospital']
        doctor = request.POST['doctor']
        report_of = request.POST['report_of']
        problem = request.POST['problem']
        report_file = request.FILES['report_file']
        
        medical_report_p = medicalreport(pname=pname, hospital_name=hospital, doctor_name=doctor, report_of=report_of, specifed_problem=problem, report_file=report_file)
        medical_report_p.save()
        return redirect("/medicalreport")
    else:
        return redirect("/medicalreport")
        
