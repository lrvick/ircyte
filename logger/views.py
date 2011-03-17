from django.shortcuts import render_to_response
from django.template import RequestContext
from logger.models import Log
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core import serializers

def index(request):
    return render_to_response('logger/index.html', (), context_instance=RequestContext(request))

def logview(request, channel):
    clogs = Log.objects.filter(channel="#"+str(channel))
    
    paginator = Paginator(clogs, 50)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        logs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        logs = paginator.page(paginator.num_pages)
    
    return render_to_response('logger/log_list.html', {
        'logs': logs,
        'logcount': clogs.count(),
    }, context_instance=RequestContext(request))


def userview(request, nick):
    logsf = Log.objects.filter(nick=nick)
    paginator = Paginator(logsf, 100)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        logs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        logs = paginator.page(paginator.num_pages)
    
    return render_to_response('logger/user.html', {
        'logs': logs,
        'logcount': logsf.count(),
    }, context_instance=RequestContext(request))


#def liveupdate(request, id):
#    response = HttpResponse()
#    response['Content-Type'] = "text/javascript"
#    response.write(serializers.serialize("json", Log.objects.filter(pk__gt=id)[:20]))
#    return response
