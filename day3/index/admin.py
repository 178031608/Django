from django.contrib import admin
from .models import *


# 声明高级管理类
class AuthorAdmin(admin.ModelAdmin):
	# 1.指定在列表页中显示的字段们
	list_display = ['names', 'age', 'email','id']
	# 2.指定能链接到详情页的字段们
	list_display_links = ['names', 'email']
	# 3.指定在类表页中被编辑的字段们
	list_editable = ['age']
	# 4.添加允许被搜索的字段们
	search_fields = ['names', 'email']
	# 5.增加爱右侧过滤器，实现快速筛选
	list_filter = ['names', 'email']
	# # 7.指定字段的分组
	# fieldsets = (
	# 	(
	# 		'基本信息', {
	# 			'fields': ('names', 'email'),
	# 		}
	# 	),
	# 	(
	# 		'可选信息', {
	# 			'fields': ('age', 'isActive'),
	# 			'classes': ('collapse',),
	# 		}
	# 	)
	# )


# 编写Book的高级管理类
class BookAdmin(admin.ModelAdmin):
	# 1.增加时间排序
	date_hierarchy = 'publicate_data'
	# 1.增加列表页中显示的字段们
	list_display = ['title','publicate_data','publisher','id',]
	# 3.增加点击详情页的功能
	list_display_links = ['title','publisher']
	# 4.增加可修改的字段
	list_editable = ['publicate_data']

# 编写publisher的高级管理类
class PublisherAdmin(admin.ModelAdmin):
	# 1.在列表页中显示的字段们
	list_display = ['name', 'address', 'city', 'website','id']
	list_display_links=['name','website']
	# 2.address 和 city　是可编辑的
	list_editable = ['address', 'city']
	# 3.右侧增加过滤器，允许按照address和city进行筛选
	list_filter = ['address', 'city']
	# 4.分组显示
	# fieldsets = (
	# 	(
	# 		'基本信息', {
	# 			'fields': ('name', 'address', 'city'),
	# 		}
	# 	),
	# 	(
	# 		'可选选项', {
	# 			'fields': ('country', 'website'),
	# 			'classes':('collapse',),
	# 		}
	# 	)
	# )


# Register your models here.

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Wife)
