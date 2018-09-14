from django.shortcuts import render

# Create your views here.
def mainprofile(request):
    return  render(request,'Teachers/mainpage.html')

def editprofile(request):
    return render(request,'Teachers/editpage.html')