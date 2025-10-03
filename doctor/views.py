from django.shortcuts import render

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import DoctorData
from django.contrib.auth import authenticate , login
from django.contrib.auth.hashers import make_password

def doctor_signup(request):
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
        
        # if User.objects.filter(username = username).exists():
        #     return render(request , 'signup.html',{'error': 'Username already exits !'})
            
        # if User.objects.filter(email = email).exists():
        #     return render(request , 'signup.html',{'error':'email already exits !'})

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name, 
            username = username, 
            email = email, 
            password=make_password(password)
        )

        DoctorData.objects.create(
            user = user, 
            profile_pic = profilePic,
            line1 = address_line1,
            city = city, 
            state = state, 
            pincode = pincode
        )
        
        return redirect('doctor_login')

    return render(request,'signup.html' ,{'error' :"" , 'success':""})


def doctor_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username,password)
        user = authenticate(request,username = username , password = password)

        print(user)

        if user is not None:
            login(request, user)
            return redirect('doctor_dashboard')
        else:
            return render(request, "login.html", {"error": "Invalid username or password"})
    
    return render(request,'login.html' ,{"error" :""})

def doctor_dashboard(request):
    doctor = DoctorData.objects.get(user= request.user)

    info = {
        "user" : request.user,
        "doctorInfo" : doctor
    }

    return render(request,'doctor_dashboard.html', info)




    
