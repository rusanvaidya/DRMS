from urllib import request
from django.shortcuts import redirect, render
from account.models import info_patient, info_hospital, info_doctor


def appointments(request):
    try:
        email = request.session['email']
        user_patient = info_patient.objects.filter(email=email)
        user_doctor = info_doctor.objects.filter(email=email)
        user_hospital = info_hospital.objects.filter(email=email)
        all_doctors = info_doctor.objects.all()
        if user_patient.exists():
            return render(request, 'appointments.html', {'email': email, 'user_as': 'patient', 'all_doctors' : all_doctors})
        if user_doctor.exists():
            return render(request, 'appointments.html', {'email': email, 'user_as': 'doctor', 'all_doctors' : all_doctors})
        if user_hospital.exists():
            return render(request, 'appointments.html', {'email': email, 'user_as': 'hospital', 'all_doctors' : all_doctors})
    except:
        if 'email' in request.session:
            email = request.session['email']
            return render(request, 'appointments.html', {'email': email})
        else:
            return redirect("/login")
        