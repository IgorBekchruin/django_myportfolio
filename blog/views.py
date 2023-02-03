from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from django.urls import reverse_lazy, reverse

from .models import Post, Comment
from .forms import CommentForm


class PostList(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'
    

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs["slug"]

        form = CommentForm()
        post = get_object_or_404(Post, slug=slug)
        comments = post.comment_set.all()

        context['post_detail'] = post
        context['form'] = form
        context['comments'] = comments
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        self.object = self.get_object()
        context = super().get_context_data(**kwargs)

        post = Post.objects.get(slug=self.kwargs['slug'])
        comments = post.comment_set.all()

        context['post_detail'] = post
        context['comments'] = comments
        context['form'] = form

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            description = form.cleaned_data['description']

            comment = Comment.objects.create(name=name, email=email, description=description, post=post)
            
            form = CommentForm()
            context['form'] = form
            return self.render_to_response(context=context)

        return self.render_to_response(context=context)
