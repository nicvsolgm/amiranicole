from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
from django.core.mail import send_mail
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


def about(request):
    return render(request, 'about.html', {})

def services(request):
    return render(request, 'services.html', {})

def work(request):
    return render(request, 'work.html', {})

def blog(request):
    return render(request, 'blog.html', {})

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        contact.name=name
        contact.email = email
        contact.subject = subject
        contact.save()
       # return HttpResponse("<h2>Thanks for contacting us</h2>")
       # send_mail(
       #     name,
       #     email,
       #     ['nicvsolgm@gmail.com'],
       # )
    return render(request, 'contact.html')

