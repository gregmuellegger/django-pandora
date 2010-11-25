from django.conf.urls.defaults import *
from django.shortcuts import render_to_response


def index(request):
    from pandora import box
    return render_to_response('index.html', box)


urlpatterns = patterns('',
    url(r'^$', index),
)
