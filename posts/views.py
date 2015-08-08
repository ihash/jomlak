from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from .models import Post

class MakePost(View):

    @staticmethod
    def get(request):

        return render(request, 'main.html', context={})


    @staticmethod
    def post(request):
        post_t = request.POST['post_text']
        return HttpResponse(post_t)

class SubmitPost(View):

    @staticmethod
    def get(request):
        post_t = Post(text=request.GET['post_text'])
        Post.objects.get(id=4)
        post_t.save()
        return HttpResponse(post_t.text)
