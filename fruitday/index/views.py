from django.shortcuts import render
from .models import *
from django.http import HttpResponse

# Create your views here.

def login_views(request):
	return render(request, 'login.html')


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
		phones = Users.objects.all()
		for phon in phones:
			if phone == phon.uphone:
				sms = '手机号已被注册'
			else:
				obj = Users(uphone=phone,upwd=pwd,uname=name,uemail=email)
				obj.save()
			return HttpResponse('OK')
		
	return render(request, 'register.html',locals())
