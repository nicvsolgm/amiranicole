from .models import Contact
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from blog.models import Post
from .forms import ContactForm
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    #context = {
    #    'form': form,
    #    'posts': Post.objects.all(),
    #    'post18': Post.objects.get(pk=18),
    #    'post19': Post.objects.get(pk=19),
    #    'post20': Post.objects.get(pk=20),
    #}

    return render(request, 'website/home.html')# context)


def about(request):
    return render(request, 'website/about.html', {})


def services(request):
    return render(request, 'website/services.html', {})


def work(request):
    return render(request, 'website/work.html', {})


def contact(request):

    if request.method == 'POST':
        name = request.POST.get('Full-name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, subject, message)

        send_mail(
            subject,
            message,
            'nicvsolgm@gmail.com',
            ['nusolmayor@gmail.com'],
            fail_silently=False,
        )

#        return HttpResponseRedirect(reverse('home'))
#    else:
#        return HttpResponse('Invalid request')
    #    data = {
    #        'name': name,
    #        'subject': subject,
    #        'email': email,
    #        'message': message
    #    }
    #    message = ''''
    #     New message: {}

     #    From: {}
     #   '''.format(data['message'],data['email'])
     #   send_mail(data['subject'],data['message'],'',['nicvsolgm@gmail.com'])
        #return render(request, 'website/contact.html', {'name': name})

   # else:
    return render(request, 'website/contact.html', {})

def skin(request):
    return render(request, 'website/skin.html', {})