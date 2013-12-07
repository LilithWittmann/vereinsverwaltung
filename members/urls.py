from django.conf.urls import *
from .views import *

urlpatterns = patterns('',
						url(r'^$', members_overview, name='members_overview'),
						url(r'^create/$', member_create, name='member_create'),
						url(r'^edit/(?P<id>[-\w]+)/$', member_edit, name='member_edit'),
						url(r'^delete/(?P<id>[-\w]+)/$', member_delete, name='member_delete'),
                       )