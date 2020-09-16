from rest_framework import serializers
from blog.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):

    username = serializers.SerializerMethodField('get_username_from_author')
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'date_updated' ,'username']

    def get_username_from_author(self, blogpost):
        username = blogpost.author.username
        return username