# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.defaultfilters import striptags
from django.utils.html import escape
from django.utils.http import urlencode
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from .models import Member
from .forms import MemberForm
from django.contrib import messages


@login_required
def members_overview(request):
    members = Member.objects.all()
    return TemplateResponse(request, "members_overview.html", {"members": members})

@login_required
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            form = MemberForm()
            messages.success(request, "Mitglied angelegt!")

    else:
        form= MemberForm()

    return TemplateResponse(request, 'member_create_edit.html',{
        "form": form,
        })


@login_required
def member_edit(request, id):
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=Member.objects.filter(id=id).get())
        if form.is_valid():
            form.save()
            messages.success(request, "Mitglied bearbeitet")
            return HttpResponseRedirect(reverse('members_overview'))
    else:
        form = MemberForm(instance=Member.objects.filter(id=id).get())
    return TemplateResponse(request, 'member_create_edit.html',{
        "form": form,
        })


@login_required
def member_delete(request, id):
    Member.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('members_overview'))

