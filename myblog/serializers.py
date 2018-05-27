from django.contrib.auth.models import User, Group
from rest_framework import serializers
from myblog.models import Post, Category
"""
serializer for myblog

Example API use
---------------
bash% # set username/password for the server
bash% USER=<user>
bash% PASSWORD=<password>
bash% # list all posts
bash% curl -H 'Accept: application/json; indent=4' -u ${USER}:${PASSWORD} http://127.0.0.1:800/myblog/post-api/
bash% # create a post
bash% curl POST http://127.0.0.1:8000/myblog/post-api/ -u ${USER}:${PASSWORD} -H "Content-Type:application/json" -d '{"title": "curld title", "text": "curld text", "author": "http://127.0.0.1:8000/myblog/users/1/", "published_date": "2018-05-26T22:22:22.766866Z"}'
bash% # list a specific post
bash% curl -H 'Accept: application/json; indent=4' -u ${USER}:${PASSWORD} http://127.000/myblog/post-api/1/
"""


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author', 'created_date', 'modified_date', 'published_date']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')