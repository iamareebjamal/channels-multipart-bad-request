from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def handler(request):
    return HttpResponse("Hello World")
