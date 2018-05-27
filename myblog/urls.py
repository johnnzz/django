"""
myblog URL configuration

Examples:
    list all posts:
        http://192.168.1.209:8000/myblog/post/
    list a specific post:
        http://192.168.1.209:8000/myblog/post/9/
    enter a new post:
        http://192.168.1.209:8000/myblog/post/create/
"""
from django.conf.urls import url, include
from myblog.views import list_view, detail_view, post_new, go_list_view, UserViewSet, GroupViewSet, PostViewSet
from django.contrib import admin
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'post-api', PostViewSet)


urlpatterns = [
    url(r'^$', go_list_view, name="go_list_view"),
    url(r'^myblog/$', go_list_view, name="go_list_view"),
    url(r'^post/$', list_view, name="blog_index"),
    url(r'^post/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^post/create/$', post_new, name="post_new"),
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    ]
