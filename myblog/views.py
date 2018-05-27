from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from myblog.models import Post, Category
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myblog.serializers import UserSerializer, GroupSerializer, PostSerializer
from .forms import MyForm
from django.utils import timezone


def go_list_view(request):
    """
    redirect user to the list view by default
    """
    return redirect("/myblog/post/")


def post_new(request):
    """
    create a new post
    """
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(detail_view, post_id=post.id)
    else:
        form = MyForm()
    return render(request, 'post.html', {'form': form})


def list_view(request):
    """
    list all the posts
    """
    #published = Post.objects.exclude(published_date__exact=None)
    published = Post.objects
    posts = published.order_by('-published_date')
    template = loader.get_template('list.html')
    context = {'posts': posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html") 


def detail_view(request, post_id):
    """
    list a specific post
    """
    #published = Post.objects.exclude(published_date__exact=None)
    published = Post.objects

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'detail.html', context)


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
