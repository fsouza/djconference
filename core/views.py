# Create your views here.
from core.forms import ConferenceForm
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def new_conference(request):
    form = ConferenceForm()
    if request.method == 'POST':
        form = ConferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('list_conferences'))
    return render_to_response('new_conference.html', {
        'form' : form
        }, context_instance=RequestContext(request)
    )
