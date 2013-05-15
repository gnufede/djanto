# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

from django.shortcuts import render

from polls.models import Poll

def index(request):
#    return HttpResponse("Hello, world. You're at the poll index.")
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
#    template = loader.get_template ('polls/index.html')
#    context = Context({
#        'latest_poll_list': latest_poll_list,
#    })
    return HttpResponse(template.render(context))

#    output = ', '.join([p.question for p in latest_poll_list])
#    return HttpResponse(output)

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
