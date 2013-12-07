from django.db import models

class Document(models.Model):
	name = models.CharField(max_length=40, verbose_name="Name")
	data = models.TextField(verbose_name="Dokument")
	def __unicode__(self):
		return self.name
