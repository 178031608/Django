from django.shortcuts import render
from .models import *

# Create your views here.

def login_views(request):
	return render(request, 'login.html')


def register_views(request):
	if request.method == 'POST':
		phone = request.POST['zphone']
		phones = Users.objects.all()
		for phon in phones:
			if phone == phon.uphone:
				sms = '手机号已被注册'
			else:
				pass
		
	return render(request, 'register.html',locals())
