# Create your views here.
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.defaultfilters import striptags
from django.utils.html import escape
from django.utils.http import urlencode
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from .utils import sync_figo_transactions
from .models import Transaction

@login_required
def transactions_overview(request):
    transactions = Transaction.objects.all()
    return TemplateResponse(request, "transactions_overview.html", {"transactions": transactions})


