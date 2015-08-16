import telegram

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
        post_t.save()
        print(post_t)
        return HttpResponse(post_t.text)


class PostListView(View):

    @staticmethod
    def get(request):
        p_list = Post.objects.all()

        return render(request, 'post_list.html', {'posts': p_list})


class LikePostView(View):

    @staticmethod
    def get(request, asha):
        p = Post.objects.get(id=int(asha))
        p.likes += 1
        p.save()
        return HttpResponse('you liked!')


class Bot(View):

    @staticmethod
    def post(request):
        bupdate = request.POST['Update']
        # print(bupdate)
        post = Post(text=bupdate)
        post.save()
        # bot = telegram.Bot(token='120382199:AAFasWEvkSBsRwQLnDbXOyFytS7SHo0PBiQ')
        # bot.sendMessage(chat_id=int(bupdate), text='Server bot response!')
        HttpResponse('halleh')