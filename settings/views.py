from django.shortcuts import render
from account.models import info_patient, info_hospital, info_doctor

# Create your views here.
def settings(request):
    email = request.session['email']
    return render(request, 'settings.html', {'email': email})

def profile(request):
    email = request.session['email']
    user_patient = info_patient.objects.filter(email=email)
    return render(request, 'profile.html', {'email': email, 'user_patient': user_patient})

def security(request):
    email = request.session['email']
    return render(request, 'security.html', {'email': email})

def report_problem(request):
    email = request.session['email']
    return render(request, 'reproblem.html', {'email': email})
