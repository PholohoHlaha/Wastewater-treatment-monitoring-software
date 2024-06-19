from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

def index(request):
    return render(request, "landing.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # User is authenticated, login
            login(request, user)
                
                # Redirect based on user role
            if username == 'operator':
                return render(request, 'operator/operator.html')
            elif username == 'lab_worker':
                return render(request, 'lab/lab_worker.html')
        else:
            return HttpResponse("Invalid role.")
        
    else:
        # Authentication failed
        messages.success("Invalid credentials. Please try again.")

def tertiary_view(request):
    return render(request, "tertiary.html")

def secondary_view(request):
    return render(request, "secondary.html")

def primary_view(request):
    return render(request, "primary.html")

def primary_analys(request):
    return render(request, "visualization/core/chart.html")

def secondary_analys(request):
    return render(request, "visualization/core/chart2.html")

def tertiary_analys(request):
    return render(request, "visualization/core/chart.html")

def predict_view(request):
    return render(request, "machine_learning/predict.html")



    