from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime 
from home.models  import Contact
from django.contrib import messages
from home.models import Register
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password


def index(request):

    context = {
        "variable1": "This is Harendra Barot. I'm learing Django with Codewithharry",
        "variable2": "I've started learning python since last"
        " week"
    }
    return render(request, 'index.html', context)
    # return HttpResponse('This is Home PAge')


def checkout(request):
    return render(request,'checkout.html')

def about(request):
    return render(request,'about.html')


def products(request):
    return render(request,'products.html')


def portfolio(request):
    return HttpResponse(request,'This is Portfolio Page')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        # attachment = request.FILES.get('attachment')


        contact = Contact(
            name=name, 
            email=email, 
            phone=phone, 
            subject=subject, 
            message=message, 
            # attachment=attachment, 
            date= datetime.today()
        )
        contact.save()
        messages.success(request, "Thank you for reaching out! Your message has been successfully received. Our team will review your inquiry and get back to you as soon as possible. Have a great day!")
        # datetime.today()
    return render(request,'contact.html')

def login_register(request):
    # Combined view handling both forms
    if request.method == "POST":
        form_type = request.POST.get('form_type', None)
        
        # Handle Registration
        if form_type == 'register':
            username = request.POST.get('username')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            print(f"Registration attempt: {email}")

            # Validate all fields
            if not all([username, email, phone, password]):
                messages.error(request, "All registration fields are required!")
                return redirect("login_register")

            # Check existing users
            if Register.objects.filter(email=email).exists():
                messages.error(request, "Email already exists!")
                return redirect("login_register")

            if Register.objects.filter(phone=phone).exists():
                messages.error(request, "Phone number already exists!")
                return redirect("login_register")

            # Create user with hashed password
            try:
                user = Register.objects.create(
                    username=username,
                    email=email,
                    phone=phone,
                    password=make_password(password), 
                    date=datetime.today()
                )
                # Create a corresponding User object
                User.objects.create_user(username=username, email=email, password=password)
                messages.success(request, "Account created successfully! Please login.")
                return redirect("login_register")
            
            except Exception as e:
                messages.error(request, f"Registration error: {str(e)}")
                return redirect("login_register")
            
        elif form_type == 'login':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            print(f"Login attempt: {username}, password={password}")

            if not username or not password:
                messages.error(request, "Email and password are required")
                return redirect("login_register")
            

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            print(user)
            
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                print("❌ Authentication failed: Invalid username or password")
                messages.error(request, "Invalid username or password")
                return redirect("login_register")

    return render(request, 'login_register.html')            

def logout_User(request):
    logout(request)
    return redirect("/login_register/")
