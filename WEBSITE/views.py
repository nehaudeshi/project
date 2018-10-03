__author__ = 'DELL'
from django.shortcuts import render,redirect
from .models import registertable,User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from Teachers.views import mainprofile
def homepage(request):
    if request.method=="POST":
       
        
        uname= request.POST.get("uname")
        name=request.POST.get("name")
        

        email= request.POST.get("email")
        psw2=request.POST.get("psw2")
        reg_type= request.POST.get("reg_type")
        #registertable.objects.all().delete()

        
        
        data={"username":uname,"email":email,"name":name,"password":psw2,"type":reg_type}
        reg = registertable(uname=uname,name=name,email=email,password=psw2,reg_type=reg_type)

        reg.save()
        User.objects.create_user(uname, email, psw2)
        user = authenticate(username = uname, password = psw2)

        if reg_type=="student":
            return render(request,'Students/main_profile.html',data)
        elif reg_type=="teacher":
            return redirect('Teachers:mainprofile')
    return render(request,'homepage.html')
def loginn(request):
    
    username = password = ''
    if request.POST:
        username = request.POST.get('uname')
        password = request.POST.get('psw')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                user=request.user
               # print(user)
                userdata=registertable.objects.get(uname=username)
               # print(userdata)
                if request.POST.get('remember'):
                    
                    #request.session.set_expiry(50)
                    
                    if userdata.reg_type=='student':
                        return render(request,"Students/main_profile.html",{'userdata':userdata})
                    elif userdata.reg_type=='teacher':
                        return redirect('Teachers:mainprofile')
                else:
                    request.session.set_expiry(30)
                    if userdata.reg_type=='student':
                        return render(request,"Students/main_profile.html")
                    elif userdata.reg_type=='teacher':
                        return redirect('Teachers:mainprofile')
                    return render(request,"homepage.html")
    return render(request,"homepage.html")
def logout(request):
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")
def email(request):
    uname=request.POST.get('uname')
    u=User.objects.get(username=uname)
    u.set_password('')
    u.save()
    uu=u.email
    print(uu)
    subject = 'Thank you for registering to our site'
    message = ' it  means a world to us '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['uu',]
    send_mail( subject, message, email_from, recipient_list )
    return render(request,'homepage.html')














    