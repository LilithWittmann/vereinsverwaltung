from django import forms
from django.forms import ModelForm
from .models import Document

class DocumentForm(ModelForm):
    class Meta:
        model = Document
   