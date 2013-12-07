# Create your views here.
from django.http import Http404, HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponsePermanentRedirect
from django.template.defaultfilters import striptags
from django.utils.html import escape
from django.utils.http import urlencode
from django.contrib.auth.decorators import login_required
from django.template.response import TemplateResponse
from django.core.urlresolvers import reverse
from django.template import Context, Template

from .models import Document
from .forms import DocumentForm
from members.models import Member


@login_required
def documents_overview(request):
    documents = Document.objects.all()
    return TemplateResponse(request, "documents_overview.html", {"documents": documents})

@login_required
def document_create(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST)
        if form.is_valid():
            form.save()
            form = DocumentForm()
    else:
        form= DocumentForm()

    return TemplateResponse(request, 'document_create_edit.html',{
        "form": form,
        })


@login_required
def document_edit(request, id):
    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=Document.objects.filter(id=id).get())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('documents_overview'))
    else:
        form = DocumentForm(instance=Document.objects.filter(id=id).get())
    return TemplateResponse(request, 'document_create_edit.html',{
        "form": form,
        })

@login_required
def document_generate(request, document_id, member_id):
    doc = Document.objects.filter(id=document_id).get()
    member = Member.objects.filter(id=member_id).get()
    if doc is None or member is None:
        return Http404

    try:
        t = Template(doc.data)
        text = t.render(Context({"member": member}))
    except:
        return HttpResponseRedirect(reverse('documents_overview'))
        
    return HttpResponse(text)


@login_required
def document_delete(request, id):
    Document.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('documents_overview'))

@login_required
def document_user_list(request, member_id):
    member = Member.objects.filter(id=member_id).get()
    documents = Document.objects.all()
    return TemplateResponse(request, 'document_user_list.html', {
        "member":member,
        "documents": documents})



