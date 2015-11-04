
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from planz.apps.planmedios.models import anunciosradio, emisora

def index_view(request):
	anu = anunciosradio.objects.all()
	emi = emisora.objects.all()

	ctx ={'emisoras': emi, 'anuncios':anu}
	return render_to_response('index.html',ctx,context_instance=RequestContext(request))
