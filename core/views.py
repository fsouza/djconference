# Create your views here.
from core.forms import ConferenceForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def new_conference(request):
    form = ConferenceForm()
    return render_to_response('new_conference.html', {
        'form' : form
        }, context_instance=RequestContext(request)
    )
