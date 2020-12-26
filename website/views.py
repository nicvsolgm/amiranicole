from django.shortcuts import render
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
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            name,
            message,
            email,
            ['nicvsolgm@gmail.com'],
        )
        return render(request, 'contact.html', {'name': name})
    else:
        return render(request, 'contact.html', {})
