__author__ = 'DELL'
from django.shortcuts import render
import pyrebase
config={
    'apiKey': "AIzaSyAjR7Zu_ruf7twHyMh-OXr183t-TceVvTY",
    'authDomain': "webst-c384e.firebaseapp.com",
    'databaseURL': "https://webst-c384e.firebaseio.com",
    'projectId': "webst-c384e",
    'storageBucket': "webst-c384e.appspot.com",
    'messagingSenderId': "251406846010"
    }
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database=firebase.database()


def homepage(request):
    if request.method=="POST":
        # print("HI")
        uname= request.POST.get("uname")
        psw2=request.POST.get("psw2")
        reg_type= request.POST.get("reg_type")
        email= request.POST.get("email")
        dept=request.POST.get("dept")
        #print(uname+" "+reg_type+" "+email)
        user=auth.create_user_with_email_and_password(email,psw2)

        uid= user['localId']

        data={"username":uname,"email":email,"dept":dept,"password":psw2}
        #print("k")
        if reg_type=="student":
            database.child("students").child(uid).set(data)
            #print("kk")
            return render(request,'Students/main_profile.html')
        elif reg_type=="teacher":
            database.child("teacher").child(uid).set(data)
            return  render(request,'Teachers/mainpage.html')
        else:
            database.child("alumni").child(uid).set(data)
        #ssif reg_type=='teacher':
            
    return render(request,'homepage.html')
def login(request):
    uname=request.POST.get("username")
    psw2=request.POST.get("password")
    email=request.POST.get("email")
    user=auth.sign_in_with_email_and_password(email,psw2)
    while database.child().child(uid).get("email")==email:
        uid=database.get(uid)
        uid=uid+1
    print(uid)
    return render(request,uid)