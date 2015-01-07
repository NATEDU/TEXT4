#coding:utf-8
from django.db import models
class company(models.Model):
	name=models.CharField(max_length=64)
	address=models.CharField(max_length=256)
	content = models.TextField()
class image(models.Model):
	name=models.CharField(max_length=64)
	img=models.ImageField(upload_to = './img')	