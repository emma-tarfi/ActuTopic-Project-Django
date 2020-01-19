from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("post_list")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("post_list")
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('sign_in')


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


@login_required(login_url='sign_in')
def post_create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('post_list')
    else:
        form = forms.CreatePost()
    return render(request, 'create_post.html', {'form': form})
