from django.conf.urls import *
from .views import *

urlpatterns = patterns('',
                        url(r'^$', transactions_overview, name='transactions_overview'),
                        url(r'^transaction-member/(?P<transaction_id>[-\w]+)/$$', transaction_to_member, name='transaction_to_member'),
                        url(r'^member-transactions/(?P<member_id>[-\w]+)/$$', member_transactions, name='member_transactions'),
                       )