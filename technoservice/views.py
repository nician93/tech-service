from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect #use for redering the html page on browser
from django.core.mail import send_mail
from django.contrib.auth.models import User
from studregistration.models import StudReg
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from moduleinformation.models import refundInfo
import datetime


@login_required(login_url='login')
def homePage(request):
    return render(request,'index.html')

def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        my_user=User.objects.filter(username=username)
        if my_user.exists():
            messages.info(request, "username already taken!")
            return redirect('signup')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            messages.info(request, "account created successfully")
            return redirect('signup')
     



    return render (request,'signup.html')


def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        if not User.objects.filter(username=username).exists(): #it checks user existence
            messages.error(request,"invaild user",extra_tags='invalid_user')
            return redirect('login')
        user=authenticate(request,username=username,password=password)
       
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"invalid password",extra_tags='invalid_password')
            return redirect('login')

    return render (request,'login.html')



'''def signupPage(request):
    if request.method=='POST':
        first_name=request.POST.get('fname')
        last_name=request.POST.get('lname')
        mother_name=request.POST.get('mname')
        father_name=request.POST.get('faname')
        p_address=request.POST.get('paddress')
        gender=request.POST.get('gender')
        state=request.POST.get('state')
        city=request.POST.get('city')
        dob=request.POST.get('dob')
        pincode=request.POST.get('pincode')
        course=request.POST.get('course')
        email=request.POST.get('email')
        password=request.POST.get('password')
        studata=StudReg(first_name=first_name,last_name=last_name,mother_name=mother_name,father_name=father_name,
                        p_address=p_address,gender=gender,state=state,city=city,dob=dob,pincode=pincode,
                        course=course,email=email,password=password)
        studata.save()
    return redirect(request,'login')

def loginPage(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        password=request.POST.get('password')
        try:
           udata1=StudReg.objects.get(email=uname)
        except StudReg.DoesNotExist:
            udata1=None
       
        if udata1:
            if udata1.password==password:
                login(request,udata1)
                return redirect('home')
            else:
                msg="password not match"
                return render(request,'login.html',{'msg':msg})
            
        else:
            msg="invalid user please sign up first"
            return render(request,'signin.html',{'msg':msg})
    return render(request,'login.html')'''


def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def contactPage(request):
    return render(request,'contactUs.html')

@login_required(login_url='login')
def sendMail(request):
    if request.method=='POST':
        subject=request.POST.get('subject')
        msg=request.POST.get('msg')
        print(subject)
    send_mail(subject,
              msg,
              "demo1150793@gmail.com",
              ["demo1150793@gmail.com"],
              fail_silently=False

    )
    return render(request,"contactUs.html")

@login_required(login_url='login')
def viewRegistrationDetail(request):
 return render(request,'hello.html')

@login_required(login_url='login')
def viewProfile(request):
    uname=request.user.username #it gets logged username
    uid=request.user.id
   # print("uid=",uid)
    dt=""
    user_instance = User.objects.get(username=uname)

    #info=StudReg.objects.raw("SELECT * FROM studregistration_studreg where uname=%s",[uname])
    if request.method=='POST':
        if 'submit1' in request.POST:
        #username=request.POST.get('uname')
            circle_name=request.POST.get('circle_name')
            refund_date=request.POST.get('refund_date')
            refund_amount=request.POST.get('refund_amount')
        

            rdata=refundInfo(refund_user=user_instance,circle_name=circle_name,refund_date=refund_date,refund_amount=refund_amount)
            rdata.save()
            messages.info(request,"Submitted successfully!")

        elif 'submit2' in request.POST:
            dt = request.POST.get('dt')
            #messages.info(request,"no data avaiable!")

    if uid==5:    
        info=refundInfo.objects.raw("SELECT * FROM moduleinformation_refundinfo where refund_date=%s",[dt])        
        userInfo={'uname':uname,'info':info,'dt':dt}
    else:
        info=refundInfo.objects.raw("SELECT * FROM moduleinformation_refundinfo where refund_date=%s and refund_user_id=%s",[dt,uid])        
        userInfo={'uname':uname,'info':info,'dt':dt}
  
    #return render(request,'profile.html',{'info':info})
    if userInfo:
     return render(request,'profile.html',userInfo)
    else:
        return render(request,'profile.html')


