from django.shortcuts import render,HttpResponse, redirect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from datetime import datetime
from home.models import Donate
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from .models import Reports, Profile
from django.http import FileResponse
import io
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib.auth .forms import UserCreationForm 
from . forms import SignUpForm, UpdateUserForm, ChangePasswordFrom, ProfilePicForm



#Generate a PDF File
def report_pdf(request):
    # Create Bytstream buffer
    buf = io.BytesIO()
    # Create a canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # Ctreate a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    # Add some lines of text
    reportss = Reports.objects.all() 
    lines = []  
    
    for reports in reportss:
       lines.append(reports.user)
       lines.append(reports.Pregnancies)
       lines.append(reports.Glucose)
       lines.append(reports.Blood_Pressure)
       lines.append(reports.Skin_Thickness)
       lines.append(reports.Insulin)
       lines.append(reports.D_P_Function)
       lines.append(reports.Age)
       lines.append(reports.Result)
       lines.append(" ")
       

    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename= 'report.pdf')   



def reports(request):
    all_Reports = Reports.objects.all()
    return render(request, 'reports.html' ,{
        'reports': all_Reports,
    })






def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def bmi(request):
    return render(request, 'bmi.html')

def donate(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        donate = Donate(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        donate.save()
        messages.success(request, "Your Application was submitted.Soon you will be get a request-call Thank You...!")
    return render(request, 'donate.html')

def predict(request):
    return render(request, 'predict.html')
def result(request):
    data = pd.read_csv(r"/home/husnain/Public/Web development/DJango/Projects/diabetes/static/diabetes.csv")
    x = data.drop("Outcome", axis=1)
    y = data["Outcome"]
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    val1=float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    pred=model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])
    result1=""
    if pred==[1]:
        result1="Positive"
    else:
        result1="Negetive"
    messages.success(request, 'You can also save your Reports by signing In...!')    
    return render(request, 'predict.html',{"result2":result1})




# ==================================================Authentication============================================================




def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have Been Logged In...!'))
            return redirect('home')
        else:
            messages.success(request, ('There was an Error , Please try again!'))
            return redirect('login')
    else:
        return render(request, 'login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been loggedout...!'))
    return redirect('home')


def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You have Registered Successfully...!'))
            return redirect('home')
        else:
            messages.success(request, ('There was an Error, Please try again...!'))
            return redirect('register')
    return render(request, 'register.html',{'form': form,})

def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id = request.user.id)
        profile_user = Profile.objects.get(user__id = request.user.id)
        user_form = UpdateUserForm(request.POST or None, request.FILES or None,instance= current_user)
        profile_form = ProfilePicForm(request.POST or None, request.FILES or None, instance= profile_user)
        if user_form.is_valid() and profile_form.is_valid():
            profile_form.save()
            user_form.save()

            login(request, current_user)
            messages.success(request, ('Your profile Has Been Updated...!'))
            return redirect('home')  
        else:
            return render(request, 'update_user.html', {'user_form': user_form, 'profile_form': profile_form})  
    else:
        messages.success(request, ('You Must Be Logged In To View That Page...!')) 
        return redirect('home') 

def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == 'POST':
            form = ChangePasswordFrom(current_user, request.POST)
            if form.is_valid():
               form.save()
               messages.success(request, ('Your password has been updated...! Please Login..'))
               return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)  
                    return redirect('update_password') 
        else:
            form = ChangePasswordFrom(current_user)
            return render(request, 'update_password.html', {'form': form})
    else:
        messages.successs(request, ('You must be loggesd in to view that page...!'))
        return redirect('home')       

       
       
    
          
       
       
       
       
       
       
        
   
   
   
   
   
   
   
   
   
 