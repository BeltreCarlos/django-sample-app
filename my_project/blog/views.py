from django.http import HttpResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import generics
import datetime


class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# Function based
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


# Function based
def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('result')


# Class based
class MyView(View):
    # Decorator
    @method_decorator(login_required)
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
