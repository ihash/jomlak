
# from django.utils import timezone
# from django.conf import settings


from django.views.generic import View
# from django.views.generic.base import ContextMixin
# from django.core.urlresolvers import reverse
# from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

class FirstView(View):

    @staticmethod
    def get(request):
        from django.conf import settings
        print(settings.BASE_DIR)
        return HttpResponse(request.GET['jk'])

class SalView(View):

    @staticmethod
    def get(request):

        return HttpResponse(request.GET['q'])
