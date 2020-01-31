from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, DeleteView, UpdateView, CreateView
from .models import Post
from django.contrib.auth.decorators import login_required
from .forms import PostForm


class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    query_pk_and_slug = True


class MyPostListView(ListView):
    queryset_draft = Post.objects.filter(status=0).order_by('-created_on')
    queryset_published = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/my_posts.html'
    model = Post
    form_class = PostForm


@method_decorator(login_required, name='dispatch')
class PostCreateView(CreateView):
    model = Post
    template_name = 'posts/create_post.html'
    form_class = PostForm
    post_created = False
    context_object_name = 'post'

    def form_valid(self, form):
        self.post_created = True
        post = form.save(commit=False)
        post.author = self.request.user
        super(PostCreateView, self).form_valid(form)
        return render(self.request, self.template_name,
                      self.get_context_data(form=form))

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['post_created'] = self.post_created
        return context

    def get_success_url(self):
        return reverse('my_posts')


@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'slug', 'image', 'content', 'status')
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
    form_class = PostForm
    success_url = reverse_lazy('my_posts')
