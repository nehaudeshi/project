from django.shortcuts import render
import pyrebase
from firebase_admin import credentials
from WEBSITE.models import userid
config={
    'apiKey': "AIzaSyAjR7Zu_ruf7twHyMh-OXr183t-TceVvTY",
    'authDomain': "webst-c384e.firebaseapp.com",
    'databaseURL': "https://webst-c384e.firebaseio.com",
    'projectId': "webst-c384e",
    'storageBucket': "webst-c384e.appspot.com",
    'messagingSenderId': "251406846010",
    'serviceAccount': "C:/Users/maitr/Downloads/webst-c384e-firebase-adminsdk-d2hqm-fcb62dae59.json",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
database=firebase.database()
# Create your views here.
def mainprofile(request):
    user = models.ForeignKey(WEBSITE.userid)
    uid=user.get('uid')
    print(uid)
    l=["students","teacher"]
    users=database.child('teacher').child('uid').get()
    dataa=dict(users.val())
    print(dataa)
    return  render(request,'Teachers/mainpage.html')
    
def editprofile(request):
	
	return render(request,'Teachers/editpage.html')



