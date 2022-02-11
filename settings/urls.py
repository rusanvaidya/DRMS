from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('settings', views.settings),
    path('profile', views.profile),
    path('security', views.security),
    path('report_problem', views.report_problem),
]