from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import PatientData
from doctor.models import BlogPost, Category
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.hashers import make_password
# Create your views here.

def patient_signup(request):
    if request.method == 'POST':
        profilePic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('confirm_password')
        address_line1 = request.POST.get('line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        

        print(first_name , last_name , username, email , password, conf_password)

        if password != conf_password:
            return render(request, 'signup.html',{'error':'passwords do not Match ! Try again'})

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name, 
            username = username, 
            email = email, 
            password=make_password(password)
        )

        PatientData.objects.create(
            user = user, 
            profile_pic = profilePic,
            line1 = address_line1,
            city = city, 
            state = state, 
            pincode = pincode
        )
        
        return redirect('patient_login')

    return render(request,'signup.html' ,{'error' :"" , 'success':""})


def patient_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username,password)
        user = authenticate(request,username = username , password = password)

        print(user)

        if user is not None:
            login(request, user)
            return redirect('Patient_dashboard')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    
    return render(request,'login.html' ,{"error" :""})


def Patient_dashboard(request):
   
    categories = Category.objects.all()

    blogs = BlogPost.objects.filter(is_draft=False)

    context = {
        "user": request.user,
        "categories": categories,
        "blogs": blogs
    }

    return render(request, 'patient_dashboard.html', context)

def patient_logout(request):
    logout(request)
    return redirect('/')





    
