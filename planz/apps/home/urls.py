__author__ = '@saksoto'

from django.conf.urls import patterns, url

urlpatterns = patterns('planz.apps.home.views', 
						url(r'^login/', 'login_view', name="login"),
						url(r'^logout/$','logout_view',name='vista_logout'),

						)