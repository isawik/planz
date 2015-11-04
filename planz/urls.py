
from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('planz.apps.planmedios.urls')),

]
