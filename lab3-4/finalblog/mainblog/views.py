from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView
from .forms import PostCreateForm
from .models import Post
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)


class HomeView(ListView):
    model = Post
    template_name = 'home.html'


def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post_form = PostCreateForm(request.POST)
            if post_form.is_valid():
                new_post = post_form.save(commit=False)
                new_post.author = request.user
                new_post.save()
                logger.info("%s created a post" % request.user.username)
                return redirect('home')
            logger.error("%s failed to create a post" % request.user.username)
            messages.error(request, "invalid data")
        else:
            post_form = PostCreateForm()
        return render(request, 'post/create.html', {'form': post_form})
    return redirect('login')


class DetailPostView(DetailView):
    model = Post
    template_name = 'post/detail.html'


def delete_post(request, slug):
    if not request.user.is_authenticated or Post.objects.filter(author=request.user, slug=slug) is None:
        raise Http404("No permission")
    Post.objects.filter(slug=slug).delete()
    logger.info("Post was deleted: %s" % slug)
    return redirect('home')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'post/update.html'
    fields = ('title', 'text')

    def get_object(self, queryset=None):
        obj = super(UpdatePostView, self).get_object(queryset)
        if obj.author != self.request.user:
            logger.error("%a was corrupted by wrong user" % obj.slug)
            raise Http404("No permission")
        return obj
