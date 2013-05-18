# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll


def index(request):
#    return HttpResponse("Hello, world. You're at the poll index.")
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
#    template = loader.get_template ('polls/index.html')
#    context = Context({
#        'latest_poll_list': latest_poll_list,
#    })
#    return HttpResponse(template.render(context))

#    output = ', '.join([p.question for p in latest_poll_list])
#    return HttpResponse(output)

def detail(request, poll_id):
    #return HttpResponse("You're looking at poll %s." % poll_id)
    
#    try:
#        poll = Poll.objects.get(pk=poll_id)
#    except Poll.DoesNotExist:
#        raise Http404
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def results(request, poll_id):
#    return HttpResponse("You're looking at the results of poll %s." % poll_id)
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def vote(request, poll_id):
#    return HttpResponse("You're voting on poll %s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Vuelve a mostrar el form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Siempre devolver un HttpResponseRedirect despues de procesar
        # exitosamente el POST de un form. Esto evita que los datos se
        # puedan postear dos veces si el usuario vuelve atrás en su browser.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
