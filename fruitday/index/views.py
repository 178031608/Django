from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .forms import *

# Create your views here.

def login_views(request):
	form = LoginForm()
	return render(request, 'login.html',locals())


def register_views(request):
	if request.method == 'POST':
		#有胡输入的手机
		phone = request.POST['zphone']
		#用户输入的密码
		pwd = request.POST['zpwd']
		#用户输入的名字
		name=request.POST['uname']
		#用户输入的邮箱
		email = request.POST['uemail']
		#判断用户是否存在，存在返回１,否则返回0
		phones = Users.objects.filter(uphone=phone)
		if phones:
			errmsg = '手机号已被注册'
			return render(request,'register.html',locals())
		else:
			try:
				obj = Users(uphone=phone,upwd=pwd,uname=name,uemail=email)
				obj.save()
			except:
				errmsg = '注册失败'
			return HttpResponse('OK')
		
	return render(request, 'register.html',locals())
