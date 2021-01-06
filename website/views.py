from .models import Contact
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from blog.models import Post

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    context = {
        'posts': Post.objects.all(),
        'post8': Post.objects.get(pk=8),
        'post9': Post.objects.get(pk=9),
        'post10': Post.objects.get(pk=10)
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html', {})


def services(request):
    return render(request, 'services.html', {})


def work(request):
    return render(request, 'work.html', {})


# def create_post(request):
#    return render(request, 'post_create.html', {})

# def blog(request):
#    header = 'Blog'
#    context = {
#        'posts': Post.objects.all(),
#        'post1': Post.objects.get(pk=1),
#        'post2': Post.objects.get(pk=2),
#
#        'header': header
#    }
#    return render(request, 'blog.html', context)

# class PostListView(ListView):
#    model = Post
#    template_name = 'website/home.html'  # <app>/<model>_<viewtype>.html
#    context_object_name = 'posts'
#    ordering = ['-date_posted']
#    paginate_by = 5

# class PostCreateView(LoginRequiredMixin, CreateView):
#    model = Post
#    fields = ['title', 'content', 'picture']
#
#    def form_valid(self, form):
#        form.instance.author = self.request.user
#        return super().form_valid(form)


def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject'],
        contact.name = name
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
