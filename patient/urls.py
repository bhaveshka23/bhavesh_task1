from django.urls import path
from . import views
urlpatterns = [
    path('signup/' , views.patient_signup, name='patient_signup'),
    path('login/' , views.patient_login, name='patient_login'),
    path('patient-dashboard/',views.Patient_dashboard, name = 'Patient_dashboard')
]
