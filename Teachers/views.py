from django.shortcuts import render

from django.db import models

from .models import edit

def mainprofile(request):
    
    return  render(request,'Teachers/mainpage.html')
    
def editprofile(request):
    if request.method=="POST":
       
        
        fname= request.POST.get("fname")
        lname=request.POST.get("lname")
        sap= request.POST.get("sap")
        contact=request.POST.get("contact")
        email= request.POST.get("email")
        profsum=request.POST.get("profsum")
        dob=request.POST.get("dob")
        print(fname)
        

        
        
        data1={"fname":fname,"lname":lname,"sap":sap,"contact":contact,"email":email,"profsum":profsum,"dob":dob}
        print(data1)
        editt = edit(fname=fname,lname=lname,sap=sap,contact=contact,email=email,profsum=profsum,dob=dob)


        editt.save()
        
        
    return render(request,'Teachers/editpage.html')

        


