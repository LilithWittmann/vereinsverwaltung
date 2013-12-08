from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'shared.views.home', name='home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',  {'template_name': 'logout.html'}, name="auth_logout"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',  {'template_name': 'logout.html'}, name="auth_logout"),
    url(r'^members/', include('members.urls')),
    url(r'^documents/', include('documents.urls')),
    url(r'^transactions/', include('transactions.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
