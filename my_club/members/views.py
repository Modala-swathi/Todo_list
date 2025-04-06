from django.http import HttpResponse
from django.template import loader
from .models import Destination

'''def members(request):
  mymembers=Member.objects.all().values()
  template=loader.get_template('all_members.html')
  context={
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context,request))
def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))'''
from django.shortcuts import render
def index(request):
    dests=Destination.objects.all()
    return render(request,'index.html',{'dests':dests})
def success(request):
    return render(request,'second.html')
def add(request):
    return render(request,'result.html',)