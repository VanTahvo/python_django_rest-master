# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Car(models.Model):
	make = models.CharField(max_length=45)
	model = models.CharField(max_length=45)
	year = models.CharField(max_length=45)
	plate = models.CharField(max_length=45)
	color = models.CharField(max_length=45)
	
	def __str__(self):
		return self.name
		

class Living(models.Model):
	city = models.CharField(max_length=45)
	district = models.CharField(max_length=45)
	house = models.CharField(max_length=45)
	heating = models.CharField(max_length=45)
	cost = models.CharField(max_length=45)

	def __str__(self):
		return self.name
		