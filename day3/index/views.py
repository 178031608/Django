from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Book, Publisher, Wife
from django.http import HttpResponseRedirect
from django.db.models import F, Q


# Create your views here.

def add_views(request):
	# 方式１
	Author.objects.create(names='张三丰', age=85)
	# 方式２
	obj = Author(names='laoshe', age=68, email='laoshe@163.com')
	obj.save()
	# 方式３
	dic = {
		'names': 'MoYan',
		'age': 59,
		'email': 'moyan@163.com',
	}
	obj = Author(**dic)
	obj.save()
	# #Insert into Book Method 1
	Book.objects.create(title='BeiYing', publicate_data='1995-2-1')
	# Insert into Book Method 2
	book = Book(title='ChaGuan', publicate_data='1968-6-18')
	book.save()
	# Insert into Book Method 3
	dic = {
		'title': 'MyQin',
		'publicate_data': '1992-10-10',
	}
	obj = Book(**dic)
	obj.save()
	# Insert into Publisher
	pub = Publisher(name='中国大学出版社', address='beijing', city='beijing', country='China', website='http://www.baidu.com')
	pub.save()
	# Insert into Publisher
	dic = {
		'name': '田间',
		'address': 'shanghai',
		'city': 'shanghai',
		'country': 'Chian',
		'website': 'http://www.qidian.com',
	}
	obj = Publisher(**dic)
	obj.save()
	return HttpResponse('Add OK')


def query_views(request):
	# #取出所有对象
	# auList = Author.objects.all()
	# s = ''
	# for au in auList:
	#     if au.email == None:
	#         s +=au.names+' '+str(au.age)+' '
	#     else:
	#         s+=au.names+' '+str(au.age)+' '+au.email
	# #取指定的列
	# au1List = Author.objects.values('names','age')
	# s = ' '
	# for au in au1List:
	#     s += '名字:'+au['names']+'年龄:'+str(au['age'])+'   '
	# #排序
	# auList = Author.objects.order_by('age')
	# for au in auList:
	#     print(au.id,',',au.names,',',au.age,',',au.email)
	# #对条件取反
	# auList = Author.objects.exclude(id=3)
	# print(auList)
	# s = ''
	# for au in auList:
	#     if au.email == None:
	#         s +=au.names+' '+str(au.age)+' '
	#     else:
	#         s +=au.names+' '+str(au.age)+' '+au.email
	
	# 查询names属性之中包含o的所有记录
	# auList = Author.objects.filter(names__contains='o')
	# # print(auList)
	# s = ''
	# for au in auList:
	#     if au.email == None:
	#         s +=au.names+' '+str(au.age)+' '
	#     else:
	#         s +=au.names+' '+str(au.age)+' '+au.email
	au = Author.objects.get(id=1)
	au.names = "老舍"
	au.age = 45
	au.email = 'laoshe@163.com'
	au.save()
	return HttpResponse('Ok')


def aulist_views(request):
	auList = Author.objects.filter(isActive=True)
	return render(request, '01_aulist.html', locals())


def delete_views(request, num1):
	# Author.objects.get(id=num1).delete()
	# 以修改数据isActiv状态值的方式来表示删除数据
	au = Author.objects.get(id=num1)
	au.isActive = False
	au.save()
	# 转发
	# return aulist_views(request)
	# 重定向
	return HttpResponseRedirect('/03_aulist/')


# 关于修改数据
def upshow_views(request, id):
	# 根据id查询指定Author的信息
	# au = Author.objects.get(id=id)
	# print(request.method)
	if request.method != 'GET':
		uname = request.POST['uname']
		uage = request.POST['uage']
		uemail = request.POST['uemail']
		print(uname,uage,uemail)
		Author.objects.filter(id=id).update(names=uname,age=uage,email=uemail)
		return HttpResponseRedirect('/03_aulist/')
	
	au = Author.objects.get(id=id)
	return render(request, '02_update.html', locals())


# 更新所有人的年龄
def upage_views(request):
	Author.objects.all().update(age=F('age') + 10)
	return HttpResponseRedirect('/03_aulist/')


def doQ_views(request):
	auList = Author.objects.filter(Q(id=6) | Q(age__gte=80), isActive=True)
	return render(request, '01_aulist.html', locals())


def raw_views(request):
	sql = 'select * from index_author where id>=8'
	auList = Author.objects.raw(sql)
	# print(aulist)
	# for au in aulist:
	#     print(au.names,',',au.age)
	return render(request, '01_aulist.html', locals())


def oto_views(request):
	# wife = Wife.objects.get(id=1)
	# author = wife.author
	# 反向查询
	# 1.获取id为22的author的信息
	author = Author.objects.get(id=23)
	# 2.在获取author的wife
	wife = author.wife
	return render(request, '03_oto.html', locals())


def otm_views(request):
	# book = Book.objects.get(id=13)
	# publisher = book.publisher
	
	publisher = Publisher.objects.get(id=10)
	books = publisher.book_set.all()
	
	return render(request, '04_otm.html', locals())


# 多对多
def mtm_views(request):
	# 通过autor查询所有的book
	author = Author.objects.get(id=22)
	books = author.book.all()
	# 通过book查询所有的author
	book = Book.objects.get(id=18)
	authors = book.author_set.all()
	# 查询韩寒的签约出版社
	hanhan = Author.objects.get(names='韩寒')
	publishers = hanhan.pusher.all()
	print(hanhan)
	# 查询北京大学出版社下所有的作者
	publisher = Publisher.objects.get(name='北京大学出版社')
	hanhans = publisher.author_set.all()
	print(hanhans)
	return render(request, '05_mtm.html', locals())


def obj_views(request):
	# count = Author.objects.auCount()
	# auList = Author.objects.lt_age(40)
	# for au in auList:
	# 	print(au.names, ',', au.age, ',', au.email)
	bookList = Book.objects.titleContains("无")
	for book in bookList:
		print(book.title)
	return HttpResponse('count')
