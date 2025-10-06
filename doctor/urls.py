from django.urls import path
from . import views
urlpatterns = [
    path('signup/' , views.doctor_signup, name='doctor_signup'),
    path('login/' , views.doctor_login, name='doctor_login'),
    path('doctor-dashboard/',views.doctor_dashboard, name = 'doctor_dashboard'),
    path('create-blog/' , views.createBlog , name='create-blog')
]
