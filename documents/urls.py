from django.conf.urls import *
from .views import *

urlpatterns = patterns('',
						url(r'^$', documents_overview, name='documents_overview'),
						url(r'^create/$', document_create, name='document_create'),
						url(r'^edit/(?P<id>[-\w]+)/$', document_edit, name='document_edit'),
						url(r'^delete/(?P<id>[-\w]+)/$', document_delete, name='document_delete'),
						url(r'^list/(?P<member_id>[-\w]+)/$', document_user_list, name='document_user_list'),
						url(r'^generate/(?P<document_id>[-\w]+)/(?P<member_id>[-\w]+)/$', document_generate, name='document_generate'),
                       )