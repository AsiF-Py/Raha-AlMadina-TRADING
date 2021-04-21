from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request,'index.html')

def contact_email(request):
    if request.method=="POST":
            email = request.POST['email']
            message = request.POST['message']
            subject = request.POST['subject']
            send_mail(
   subject,                    #Subject here
       message,                    #Here is the message.
       settings.EMAIL_HOST_USER ,  #My admin mail / from mail
       [email],                    #To mail / email
       fail_silently=False,
)    
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')