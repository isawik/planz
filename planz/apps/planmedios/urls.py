__author__ = '@saksoto'

from django.conf.urls import patterns, url

urlpatterns = patterns('planz.apps.planmedios.views', 
						url(r'^$', 'index_view', name="index"),
						)