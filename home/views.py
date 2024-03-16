from django.shortcuts import render,HttpResponse, redirect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from datetime import datetime
from home.models import Donate
from home.models import Reports
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from .models import Reports
from django.http import FileResponse
import io
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import Profile

def profile(request, pk):
    if request.user.is_authenticated:        
        profile = Profile.objects.get(user_id = pk)

        if request.method =='POST':
            current_user_profile = request.user.profile
            action = request.POST['follow']
            if action == "unfollow":
                current_user_profile.follows.remove(profile)
            elif action == "follow":
                current_user_profile.follows.add(profile)
            current_user_profile.save()    
        return render (request, "profile.html", {
            "profile": profile
        })
    else:
        messages.success(request, 'Your must be logged in to view this page....!')
        return redirect('home')
    

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





# @login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')
# @login_required(login_url='signin')
def about(request):
    return render(request, 'about.html')
# @login_required(login_url='signin')
def bmi(request):
    return render(request, 'bmi.html')
# @login_required(login_url='signin')
def donate(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        donate = Donate(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        donate.save()
    return render(request, 'donate.html')
def predict(request):
    return render(request, 'predict.html')
def result(request):
    data = pd.read_csv(r"husnain/home/Public/diabetes/static/diabetes.csv")
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
    return render(request, 'predict.html',{"result2":result1})

# def Reports(request):
#     data = pd.read_csv(r"D:\MLPlayGround\diabetes\static\diabetes.csv")
#     x = data.drop("Outcome", axis=1)
#     y = data["Outcome"]
#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
#     model = LogisticRegression()
#     model.fit(x_train, y_train)
#     if request.method=="POST":
#        Pregnancies=request.POST.get('n1')
#        Glucose =request.POST.get('n2')
#        Blood_Pressure = request.POST.get('n3')
#        Skin_Thickness= request.PSOT.get('n4')
#        Insulin = request.POST.get('n5')
#        BMI= request.POST.get('n6')
#        D_P_Function=request.POST.get('n7')
#        Age = request.POST.get('n8')
#     pred=model.predict([[Pregnancies, Glucose,Blood_Pressure,Skin_Thickness,Insulin,BMI,D_P_Function,Age]])
#     result1=""
#     report=Reports(Pregnancies=Pregnancies,Glucose=Glucose,Blood_Pressure=Blood_Pressure,Skin_Thickness=Skin_Thickness,Insulin=Insulin,BMI=BMI,D_P_Function=D_P_Function,Age=Age,Result='Your Result is +result2')
#     report.save()

  
       
       
       
       
       
       
       
       
       
       
        
   
   
   
   
   
   
   
   
   
    #   results= Reports(Pregnancies=str('n1'), Glucose=str('n2'),Blood_Pressure=str('n3'),Skin_Thickness=str('n4'),Insulin=str('n5'),BMI=str('n6'),D_P_Function=str('n7'), Age=str('n8'))
    # results.save()