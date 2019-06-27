# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class product(models.Model):
	
	title        =models.TextField(default='mm')
	description  =models.TextField(default='ss')
	price        =models.TextField(default='this is cool')