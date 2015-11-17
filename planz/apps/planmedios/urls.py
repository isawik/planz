__author__ = '@saksoto'

from django.conf.urls import patterns, url

urlpatterns = patterns('planz.apps.planmedios.views', 
						url(r'^$', 'index_view', name="index"),
						url(r'^cliente/(?P<id_prod>.*)/$','simplecliente_view',name='vista_single_cliente'),
						url(r'^camp/(?P<id_prod>.*)/$','simplecamp_view',name='vista_single_camprad'),
						url(r'^resumenradio/(?P<id_prod>.*)/$','resumenradio_view',name='vista_single_resumenradio'),
						)