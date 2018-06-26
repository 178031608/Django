from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def request_views(request):
	print(dir(request))
	return HttpResponse('Response OK')