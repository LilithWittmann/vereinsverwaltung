from django import forms
from django.forms import ModelForm
from .models import Member

class MemberForm(ModelForm):
    class Meta:
        model = Member
   