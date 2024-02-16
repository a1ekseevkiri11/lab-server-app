from django.http import HttpResponse
from django.db import connections
import django

def infoServer(request):
    return HttpResponse(django.VERSION)


def infoClient(request):
    agent = request.META['HTTP_USER_AGENT']
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    answer = ip + "<br>" + agent
    return HttpResponse(answer)


def infoDatabase(request):
    databaseName = connections['default'].settings_dict['NAME']
    return HttpResponse(databaseName)