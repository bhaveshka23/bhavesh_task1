from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import DoctorData , Category , BlogPost
from django.contrib.auth import authenticate , login , logout
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


def MyBlog(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        blogImage = request.FILES.get('blogImage')
        category_id = request.POST.get('category')
        title = request.POST.get('title')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        is_draft = True if request.POST.get('is_draft') else False

        category = Category.objects.get(id=category_id)

        BlogPost.objects.create(
            author = request.user,
            title = title,
            summary = summary,
            content = content,
            image = blogImage,
            category = category,
            is_draft = is_draft
        ) 

        return redirect('my-blogs')


    Blogs = BlogPost.objects.filter(author=request.user).select_related('category').order_by('-id')

    return render(request, 'doctor_blogs.html', { 'categories': categories, 'blogs': Blogs })


def doctor_logout(request):
    logout(request)
    return redirect('/')


def doctor_profile(request):
    doctor = get_object_or_404(DoctorData, user=request.user)

    info = {
        'doctor' : doctor
    }

    return render(request ,'doctor_profile.html' , info)






    
