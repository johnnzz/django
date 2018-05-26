"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from myblog.views import list_view, detail_view, post_new, go_list_view, UserViewSet, GroupViewSet
from django.contrib import admin
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    url(r'^$', go_list_view, name="go_list_view"),
    url(r'^myblog/$', go_list_view, name="go_list_view"),
    url(r'^post/$', list_view, name="blog_index"),
    url(r'^post/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^post/create/$', post_new, name="post_new"),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include(router.urls)),
    ]
