from rest_framework import serializers
from posts.models import Post

# Similar to Django ModelForms
# https://docs.djangoproject.com/en/2.0/topics/forms/modelforms/


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # map all model fields
