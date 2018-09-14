from django.shortcuts import render

# Create your views here.

def mainprofile(request):
    if request.method=='POST':
        pass

    return render(request,'Students/main_profile.html')

def editprofile(request):

    return render(request,'Students/edit_profile.html')

