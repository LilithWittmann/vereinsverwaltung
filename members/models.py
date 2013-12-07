# coding: utf-8
from django.db import models
from django.contrib import admin
from datetime import date

class Member(models.Model):
    forename = models.CharField(max_length=40, verbose_name="Vorname")
    surname = models.CharField(max_length=40, verbose_name="Nachname")
    phone = models.CharField(max_length=40, verbose_name="Telefon")
    email = models.CharField(max_length=40, verbose_name="E-Mail")
    street = models.CharField(max_length=40, verbose_name="Straße & Hausnummer")
    postal_code = models.CharField(max_length=40, verbose_name="Postleitzahl")
    city = models.CharField(max_length=40, verbose_name="Stadt")
    iban = models.CharField(max_length=34, verbose_name="IBAN")
    bic = models.CharField(max_length=11, verbose_name="BIC")
    next_pay_date = models.DateField(default=date.today, verbose_name="Nächster Zahlungstermin")
    yearly_amount = models.CharField(max_length=40, verbose_name="Jahresbeitrag")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s %s" % (self.forename, self.surname)

admin.site.register(Member)
