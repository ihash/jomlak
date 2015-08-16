
# from django.utils import timezone
# from django.conf import settings


from django.views.generic import View
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
