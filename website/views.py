from .models import Contact
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from blog.models import Post
from .forms import ContactForm

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
        'posts': Post.objects.all(),
        'post3': Post.objects.get(pk=3),
        'post4': Post.objects.get(pk=4),
        'post5': Post.objects.get(pk=5)
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def work(request):
    return render(request, 'work.html', {})


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, "contact.html", context)


#    if request.method == 'POST':
#        contact = Contact()
#        name = request.POST['name']
#        phone = request.POST['phone']
#        email = request.POST['email']
#        subject = request.POST['subject'],
#        contact.name = name
#        contact.phone = phone
#        contact.email = email
#        contact.subject = subject
#        contact.save()

#   return render(request, 'home.html')
