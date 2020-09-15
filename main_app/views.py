from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DeleteView, ListView 

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Profile, Article

# Create your views here.
# class Profile():
#     def __init__(self, name, email, age):        
#         self.name = name 
#         self.email = email
#         self.age = age

# profiles = [
#     Profile('Austin', 'austin@example.com', 33),
#     Profile('Dom', 'Dom@example.com', 28),
#     Profile('Diego', 'Diego@example.com', 30),
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def profiles_index(request):
    profiles = Profile.objects.filter(user=request.user)
    return render(request, 'profiles/index.html', {'profiles': profiles})

# def profiles_detail(request, profile_id):
#     profile = Profile.objects.get(id=profile_id)
#     return render(request, 'profiles/detail.html', {
#         'profile': profile,
#     })

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def articles_index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', { 'articles': articles })

def articles_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'articles/detail.html', { 'article': article })

class ArticleCreate(CreateView):
    model = Article
    fields = '__all__'

class ArticleUpdate(UpdateView):
    model = Article
    fields = '__all__'

class ArticleDelete(DeleteView):
    model = Article
    success_url = '/articles/'