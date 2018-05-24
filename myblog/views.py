from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from myblog.models import Post, Category
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myblog.serializers import UserSerializer, GroupSerializer
from .forms import MyForm
from django.utils import timezone
from django import forms


def index(request):
    return HttpResponse("Hello, world. You're at the myblog index.")


def post_new(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        return render(request, 'post.html', {'form': form})
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form = MyForm()
        return render(request, "post.html", {'form': form})


def list_view(request):
    print("Xrequest",request)
    published = Post.objects.exclude(published_date__exact=None)
    #published = Post.objects
    print("XPUB",published)
    posts = published.order_by('-published_date')
    print("XPOSTS",posts)
    template = loader.get_template('list.html')
    #context = RequestContext(request, {'posts': posts})
    context = {'posts': posts}
    body = template.render(context)
    return HttpResponse(body, content_type="text/html") 

def detail_view(request, post_id):
    #published = Post.objects.exclude(published_date__exact=None)
    published = Post.objects

    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404

    context = {'post': post}
    return render(request, 'detail.html', context)


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
