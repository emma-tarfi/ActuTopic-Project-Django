from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class MyPostListView(ListView):
    queryset_draft = Post.objects.filter(status=0).order_by('-created_on')
    queryset_published = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/my_posts.html'
    model = Post
    form_class = forms.PostForm


@login_required
def post_create(request):
    if request.method == 'POST':
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('post_list')
    else:
        form = forms.PostForm()
    return render(request, 'posts/create_post.html', {'form': form})


# @method_decorator(login_required, name='dispatch')
#  class PostCreateView(CreateView):
#     model = Post
#     template_name = 'create_post.html'
#     form_class = forms.PostForm
#
#     def get_object(self, **kwargs):
#         return get_object_or_404(User, pk=self.request.user.id)
#
#     def get_success_url(self):
#         return reverse('create')


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'slug', 'image', 'content', 'status')
    success_message = "Votre post a bien été modifié !"
    template_name = 'posts/update_post.html'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.updated_on = timezone.now()
        post.created_on = post.updated_on
        post.save()
        return redirect('my_posts')


@method_decorator(login_required, name='dispatch')
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    form_class = forms.PostForm
    success_message = "Votre post a bien été supprimé !"
    success_url = reverse_lazy('my_posts')
