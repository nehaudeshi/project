from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.db import models
from WEBSITE.models import User,registertable
from .models import edit 
@login_required
def mainprofile(request):
	print("hi")
	u=None
	editt=None
	c=None
	d=None
	if request.user.is_authenticated:
		print(request.user.username)
		c=str(request.user.username)

		d=int(c)
		if registertable.objects.filter(uname=c).exists():
			u=registertable.objects.get(uname=c)
		
		#edit.objects.all().delete()
		if edit.objects.filter(sapid=d).exists():
			editt=edit.objects.get(sapid=d)
		
		print(editt)
		
		#u=dict(u)
		
	return  render(request,'Teachers/mainpage.html',{'uu':u,'edittt':editt})
		    
    
   
def editprofile(request):
	u=None
	editt=None
	c=None
	d=None
	if request.method=="POST":
		 fname= request.POST.get('fname')
		 lname=request.POST.get('lname')
		 sapid= request.POST.get('sap')
		 contact=request.POST.get('phone')
		 email= request.POST.get('email')
		 profsum=request.POST.get('profsum')
		 dob=request.POST.get('dob')
		 if request.user.is_authenticated:
		 	print("entered")
		 	edit.objects.all().delete()
		 	data1={"firstname":fname,"lastname":lname,"sapidd":sapid,"contactinfo":contact,"emailid":email,"profsumm":profsum,"dob":dob}
		 	editt = edit(fname=fname,lname=lname,sapid=sapid,contact=contact,email=email,prof=profsum,date=dob)
		 	editt.save()
		 	c=str(request.user)
		 	d=int(c)
		 	u=registertable.objects.get(uname=c)
		 	editt = edit.objects.filter(sapid=d) 
		 	mainprofile(request)
		 	
			
	return render(request,'Teachers/editpage.html',{'uu':u,'edittt':editt})
        	
        	     
        	  	
        	
        	
    
        	
        	   
        	     	        	

        	
        	
        	
        	
    
         
         
        
        
        
        
    
       
        
        
        
			


		    
		    
			
			
		
		
		
		
		
		
		
		
		    
		
    
        
        

        
        
        

        


