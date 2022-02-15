from django.contrib import messages
from django.shortcuts import render, redirect

from .models import info_patient, info_hospital, info_doctor


def signup(request):
    return render(request, 'signup.html')


def register_patient(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        citizen_no = request.POST['citizen_no']
        password = request.POST['password']
        confirm = request.POST['re_password']
        pin = request.POST['pin']
        address = request.POST['address']

        if password == confirm:
            if info_patient.objects.filter(email=email).exists():
                messages.info(request, 'This Email is Taken')
                return redirect('/register_patient')

            else:
                user = info_patient(full_name=full_name, email=email, password=password, citizen_no=citizen_no, pin=pin, address=address)
                user.save()
                request.session['email'] = email
                return redirect('/')
        else:
            print("Password not matching")
            return redirect('/register_patient')
    else:
        return render(request, 'register_patient.html')


def register_doctor(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['re_password']
        field = request.POST['field']
        hospital = request.POST['hospital']

        if password == confirm:
            if info_doctor.objects.filter(email=email).exists():
                messages.info(request, 'This Email is Taken')
                return redirect('../register')

            else:
                user = info_doctor(full_name=full_name, email=email, password=password, field=field, hospital=hospital)
                user.save()
                request.session['email'] = email
                return redirect('/')
        else:
            print("Password not matching")
            return redirect('/register_doctor')
    else:
        return render(request, 'register_doctor.html')


def register_hospital_admin(request):
    if request.method == 'POST':
        hospital_name = request.POST['hospital_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['re_password']
        city = request.POST['city']
        hospital_pan = request.POST['pan_no']

        if password == confirm:
            if info_hospital.objects.filter(email=email).exists():
                messages.info(request, 'This Email is Taken')
                return redirect('/register_doctor')

            else:
                user = info_hospital(hospital_name=hospital_name, email=email, password=password, city=city, hospitalpan=hospital_pan)
                user.save()
                request.session['email'] = email
                return redirect('/')
        else:
            print("Password not matching")
            return redirect('/register')
    else:
        return render(request, 'register_hospital_admin.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user_patient = info_patient.objects.filter(email=email, password=password)
        if user_patient.exists():
            request.session['email'] = email
            return redirect("/")
        else:
            if info_doctor.objects.filter(email=email, password=password).exists():
                request.session['email'] = email
                return redirect("/")
            else:
                if info_hospital.objects.filter(email=email, password=password).exists():
                    request.session['email'] = email
                    return redirect("/")
    return render(request, 'login.html')


def logout(request):
    del request.session['email']
    if 'pin' in request.session:
       del request.session['pin']
    return redirect('/')