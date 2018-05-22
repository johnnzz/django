from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from myblog.models import Post, Category

def index(request):
    return HttpResponse("Hello, world. You're at the myblog index.")

def list_view(request):
    print("Xrequest",request)
    #published = Post.objects.exclude(published_date__exact=None)
    published = Post.objects
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
