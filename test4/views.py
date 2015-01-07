from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.template.response import TemplateResponse
from test4.models import company,image
import datetime
def home(request):
	return HttpResponse('Hell world')
def hello(request,id):
	t=datetime.datetime.now()
	c=company.objects.all()
	i=image.objects.get(id=1)
	all_img=image.objects.all()
	d={'time':str(t),'c':c,'i':i}
	for x in all_img:
		d[x.name]=x.img
	return	TemplateResponse(request,"test4.html",d)

def new(request):
	print request.POST
	c=company()
	c.name=request.POST['name']	
	c.address=request.POST['address']
	c.content=request.POST['content']	
	c.save()
	return redirect("/html/new")

def delete(request,id):
	c=company.objects.get(id=int(id))
	c.delete()
	return redirect("/html/del")

def edit_view(request,id):
	c=company.objects.get(id=int(id))
	d={'c':c}
	return TemplateResponse(request,'edit_view.html',d)
def edit(request,id):
	c=company.objects.get(id=int(id))
	c.name=request.POST['name']
	c.address=request.POST['address']
	c.content=request.POST['content']
	c.save()
	return redirect("/html/edit")
