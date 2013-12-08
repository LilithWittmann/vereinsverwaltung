# -*- coding: utf-8 -*-
from django.db import models
from members.models import Member
from django.contrib import admin


class Transaction(models.Model):
    value_date  = models.DateTimeField(verbose_name="Wertstellungsdatum")
    bank_name = models.CharField(max_length=40, verbose_name="Bankname") 
    booked = models.BooleanField(verbose_name=u'gebucht')
    booking_date = models.DateTimeField( verbose_name=u'Buchungsdatum')
    account_id = models.CharField(max_length=40, verbose_name="Figo Account id")  
    bank_code = models.CharField(max_length=40, verbose_name="Bankname") 
    type = models.CharField(max_length=40, verbose_name="Typ")
    purpose = models.CharField(max_length=200, verbose_name="Verwendungszweck")
    name = models.CharField(max_length=200, verbose_name="Name")
    currency = models.CharField(max_length=6, verbose_name="Währung")
    amount = models.DecimalField(verbose_name=u'Betrag', decimal_places=2, max_digits=14) 
    account_number = models.CharField(max_length=40, verbose_name="Kontonummer")
    visited = models.BooleanField(verbose_name=u'besucht')
    modification_timestamp = models.DateTimeField(verbose_name=u'Änderunsgzeitpunkt')
    creation_timestamp = models.DateTimeField(verbose_name=u'Erstellungszeitpunkt')
    transaction_id = models.CharField(max_length=40, verbose_name="Transaktionsid")
    booking_text = models.CharField(max_length=40, verbose_name="Buchungstext")
    def __unicode__(self):
        return self.purpose


admin.site.register(Transaction)
