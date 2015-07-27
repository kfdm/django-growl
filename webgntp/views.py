from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from gntp.config import GrowlNotifier


class GrowlForward(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(GrowlForward, self).dispatch(*args, **kwargs)

    def post(self, request):
        growl = GrowlNotifier(notifications=['Test'])
        growl.register()
        growl.notify('Test', 'Test', 'Test')
        return HttpResponse('result')
