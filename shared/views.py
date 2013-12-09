# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.defaultfilters import striptags
from django.utils.html import escape
from django.utils.http import urlencode
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.db import connection
from django.db.models import Count, Sum
from members.models import Member
from .models import *

@login_required
def home(request):
    truncate_date = connection.ops.date_trunc_sql('month','created_at')
    qs = Member.objects.extra({'month':truncate_date})
    member_report = qs.values('month').annotate(Count('pk')).order_by('month')
    return TemplateResponse(request, "home.html", {"member_report": member_report})