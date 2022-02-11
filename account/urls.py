from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup,name='signup'),
    path('register_patient', views.register_patient,name='register_patient'),
    path('register_doctor', views.register_doctor,name='register_doctor'),
    path('register_hospital_admin', views.register_hospital_admin,name='register_hospital_admin'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
]