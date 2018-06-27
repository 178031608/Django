from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.

def request_views(request):
	# print(dir(request))
	# return HttpResponse('Response OK')
	
	scheme = request.scheme
	body = request.body
	host = request.get_host()
	path = request.path
	method = request.method
	get = request.GET
	post = request.POST
	cookies = request.COOKIES
	return render(request, '01_request.html', locals())


def login_views(request):
	if request.method == 'GET':
		return render(request,'02_login.html')
	else:
		uname = request.POST['uname']
		upwd = request.POST['upwd']
		print(uname,upwd)
		return HttpResponse('用户名:'+uname+', 密码：'+upwd)


def get_views(request):
	uname = request.GET.get('uname','')
	upwd = request.GET.get('upwd','')
	
	if uname and upwd:
		return  HttpResponse('用户名:'+uname+'密码:'+upwd)
	else:
		return  render(request,'03_login.html')
	
def query_views(request):
	id = request.GET.get('id','')
	name = request.GET.get('name','')
	return HttpResponse('id:'+id+'name:'+name)

def form_views(request):
	if request.method == 'GET':
		form = RemarkForm()
		return render(request,'04_form.html', locals())
	else:
		#将post的数据交给RemarkForm()
		form = RemarkForm(request.POST)
		#要通过验证
		if form.is_valid():
			#通过cleaned_data取值
			cd = form.cleaned_data
			return HttpResponse(cd['subject']+cd['email'])
		
def register_views(request):
	if request.method == 'GET':
		form = RegisterForm()
		return render(request,'05_register.html',locals())
	else:
		form = RegisterForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			users = Users(**cd)
			users.save()
			return HttpResponse('Register OK')
		
def modelForm_views(request):
	pass