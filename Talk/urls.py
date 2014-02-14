from django.conf.urls import patterns, include, url
from Main.views import *
from django.contrib import admin
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', main_page),
    url(r'^JoinNewPerson/', new_member),
    url(r'^JaehongTalk/', talk_page),
    url(r'^UserIdentitySave/', UserIdentitySave),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^register/$', register),

    # url(r'^Talk/', include('Talk.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
