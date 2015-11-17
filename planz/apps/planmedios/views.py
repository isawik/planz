
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from planz.apps.planmedios.models import anunciosradio, emisora, cliente, campanaradio, productocliente, grupo
from planz.settings import URL_LOGIN
from django.contrib.auth.decorators import login_required

@login_required(login_url=URL_LOGIN)
def index_view(request):
	proc = productocliente.objects.all()
	cli = cliente.objects.all()
	camp = campanaradio.objects.all()
	anu = anunciosradio.objects.all()
	emi = emisora.objects.all()
	for a in anu.all():
		dato1 = a.dias
		dato2 = a.emisora.alcance
		total = (float(dato1) + float(dato2))
	ctx ={'emisoras': emi, 'anuncios':anu, 'total':total, 'cliente':cli, 'camp':camp}
	return render_to_response('index.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def simplecliente_view(request,id_prod):
	cli = cliente.objects.get(id=id_prod)
	prodcli = cli.producto.all()
	ctx = {'cliente':cli,'prodcli':prodcli}
	return render_to_response('simplecliente.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def simplecamp_view(request,id_prod):
	camprad = campanaradio.objects.get(id=id_prod)
	camp = campanaradio.objects.all()
	gru = grupo.objects.all()
	campanun = camprad.anuncios.all()
	ctx = {'camprad':camprad,'campanun':campanun,'gru':gru, 'camp':camp}
	return render_to_response('simplecamp.html',ctx,context_instance=RequestContext(request))

@login_required(login_url=URL_LOGIN)
def resumenradio_view(request,id_prod):
	emi = emisora.objects.get(id=id_prod)
	ctx = {'emi':emi}
	return render_to_response('resumenradio.html',ctx,context_instance=RequestContext(request))
