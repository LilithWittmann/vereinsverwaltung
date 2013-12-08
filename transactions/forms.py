from django import forms
from django.forms import ModelForm
from .models import Transaction

class TransactionMemberForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['member']
   