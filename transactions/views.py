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
from .forms import TransactionMemberForm
from members.models import Member

@login_required
def transactions_overview(request):
    transactions = Transaction.objects.all()
    return TemplateResponse(request, "transactions_overview.html", {"transactions": transactions})


def transaction_to_member(request, transaction_id):
    if request.method == 'POST':
        form = TransactionMemberForm(request.POST, instance=Transaction.objects.filter(id=transaction_id).get())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('transactions_overview'))
    else:
        form = TransactionMemberForm(instance=Transaction.objects.filter(id=transaction_id).get())
    return TemplateResponse(request, 'transaction_to_member.html',{
        "form": form,
        })



def member_transactions(request, member_id):
    member = Member.objects.filter(id=member_id).get()
    transactions = Transaction.objects.filter(member=member)
    return TemplateResponse(request, 'member_transactions.html',{
        "member": member,
        "transactions": transactions
        })