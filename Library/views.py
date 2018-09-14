from django.shortcuts import render
from .models import Tech_Model,Chem_Model,Elec_Model,Mech_Model,Bio_Model
# Create your views here.

def tech(request):

    books = Tech_Model.objects.all()
    print(books)



    if request.method=='POST':

        print("POST request")
        return render(request, 'Library/library-tech.html',{'books':books})


    print("GET request")

    return render(request,'Library/library-tech.html',{'books':books})


def bio(request):

    books = Bio_Model.objects.all()
    if request.method=='POST':
        print("POST request")
        return render(request, 'Library/library-bio.html')


        #print("GET request")

    return render(request,'Library/library-bio.html',{'books':books})

def elec(request):

    books = Elec_Model.objects.all()
    if request.method=='POST':
        print("POST request")
        return render(request, 'Library/library-elec.html')


        #print("GET request")

    return render(request,'Library/library-elec.html',{'books':books})

def mech(request):

    books = Mech_Model.objects.all()
    if request.method=='POST':
        print("POST request")
        return render(request, 'Library/library-mech.html')


        #print("GET request")

    return render(request,'Library/library-mech.html',{'books':books})

def chem(request):

    books = Chem_Model.objects.all()
    issued = Chem_Model.objects.filter('issued')
    copies = Chem_Model.objects.filter('copies')



    if request.method=='POST' and copies != 0:
        c = Chem_Model()
        c.copies = copies-1
        c.save()
        print("POST request")
        return render(request, 'Library/library-chem.html')


        #print("GET request")

    return render(request,'Library/library-chem.html',{'books':books})
