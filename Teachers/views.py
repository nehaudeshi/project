from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import models

from .models import edit

def mainprofile(request):
	if request.user.is_authenticated:
		u=user.object.get(uname=request.user)
		print(u)
	return  render(request,'Teachers/mainpage.html')
		    
    
   
def editprofile(request):
    if request.method=="POST":
        fname= request.POST.get('fname')
        lname=request.POST.get('lname')
        sapid= request.POST.get('sap')
        contact=request.POST.get('phone')
        email= request.POST.get('email')
        profsum=request.POST.get('profsum')
        dob=request.POST.get('dob')
        print(request.user)
        
        if request.user.is_authenticated:
        	print("entered")
        	data1={"firstname":fname,"lastname":lname,"sapidd":sapid,"contactinfo":contact,"emailid":email,"profsumm":profsum,"dob":dob}
        	editt = edit(fname=fname,lname=lname,sapid=sapid,contact=contact,email=email,prof=profsum,date=dob)
        	editt.save()
        	return render(request,'Teachers/mainpage.html', data1)
        '''else:
        	return HttpResponse'''
        	
    return render(request,'Teachers/editpage.html')
			


		    
		    
			
			
		
		
		
		
		
		
		
		
		    
		
    
        
        

        
        
        

        


