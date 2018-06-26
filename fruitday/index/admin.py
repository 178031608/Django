from django.contrib import admin
from .models import *
# Register your models here.

#声明用户高级管理类
class UserAdmin(admin.ModelAdmin):
	#1.用于展示的字段们
	list_display = ['id','uname','uphone','isActive']
	#2.可编辑的字段
	list_editable = ['isActive']
	#3.可链接到详情页的字段们
	list_display_links = ['id','uname','uphone']
	#4.允许被搜索的字段们
	search_fields = ['id','uname']
	
	
	
#声明商品的高级管理类
class GoodsAdmin(admin.ModelAdmin):
	#1.用于展示的字段们
	list_display = ['title','price','isActive']
	#2.可编辑的字段
	list_editable = ['isActive']
	#3.可链接到详情页的字段恩
	list_display_links = ['title','price']
	#4.允许被搜索的字段们
	search_fields = ['id','title','price']
	
	
#声明商品类型的高级管理类
class GoodsTypeAdmin(admin.ModelAdmin):
	#1.用于展示的字段们
	list_display = ['title','picture','desc']
	#2.可链接到详情页的字段们
	list_display_links = ['title']
	#3.可以被修改的字段们
	list_editable = ['picture','desc']
	#3.允许被搜索的字段们
	search_fields = ['title','id']
#注册进后台管理
admin.site.register(Users,UserAdmin)
admin.site.register(GoodsType,GoodsTypeAdmin)
admin.site.register(Goods,GoodsAdmin)
