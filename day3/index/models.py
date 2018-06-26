from django.db import models


# 声明自定义的objects - models.Manager
class AuthorManager(models.Manager):
	def auCount(self):
		return self.all().count()
	
	# 查询年纪小于指定年纪的作者的信息
	def lt_age(self, age):
		return self.filter(age__lt=age)
	
class BookManager(models.Manager):
	# 添加函数,查询属性名包含指定关键字的书籍的信息
	def titleContains(self, keywords):
		return self.filter(title__contains=keywords)
	

class Publisher(models.Model):
	name = models.CharField(max_length=30, verbose_name='出版社名字')
	address = models.CharField(max_length=50, verbose_name='出版社地址')
	city = models.CharField(max_length=20, verbose_name='出版社城市')
	country = models.CharField(max_length=20, verbose_name='出版社国家')
	website = models.URLField(verbose_name='出版社网址')
	
	# 修改后台管理页中对应的名称
	def __str__(self):
		return self.name
	
	class Meta:
		# 1.更改表名为publisher
		db_table = 'publisher'
		# 修改其展示名称为出版社
		verbose_name = '出版社'
		verbose_name_plural = verbose_name


# 创建Book模型类
# title,书名,publicate_data,出版时间
class Book(models.Model):
	# 重新指定objects
	objects = BookManager()
	title = models.CharField(max_length=50, verbose_name='书名')
	publicate_data = models.DateField(verbose_name='出版时间')
	# 增加publisher的引用(1:M)
	publisher = models.ForeignKey(Publisher, null=True, verbose_name='出版社')
	
	# 修改后台管理页中，每个对象的名称
	def __str__(self):
		return self.title
	
	class Meta:
		# 修改表明
		db_table = 'book'
		# 修改其展示名称
		verbose_name = '书籍'
		verbose_name_plural = verbose_name
		# 按照出版时间降序排序
		ordering = ['-publicate_data']


# 创建Author模型类
# name,姓名,age,年龄,emalil,邮箱
class Author(models.Model):
	objects = AuthorManager()
	names = models.CharField(max_length=30, verbose_name='作者名字')
	age = models.IntegerField(verbose_name='作者年龄')
	email = models.EmailField(null=True, verbose_name='作者邮箱')
	# 增加一个状态列，表示用户是启用还是精致，默认为True表示启动
	isActive = models.BooleanField(default=True, verbose_name='作者状态')
	# 增加一个对Book的多对多的引用
	book = models.ManyToManyField(Book)
	pusher = models.ManyToManyField(Publisher)
	
	def __str__(self):
		return self.names
	
	# 声明内部类，来定义但前类在管理页面中的展现形式
	class Meta:
		# 1.修改表明为authors
		db_table = 'author'
		# 修改实体类在后台管理园中的名称(单数)
		verbose_name = '作者'
		# 修改实体类在后台管理中的名称(复数)
		verbose_name_plural = verbose_name
		# 4.首先按照年龄降序排序，其次按照id升序排序
		ordering = ['-age', 'id']


class Wife(models.Model):
	names = models.CharField(max_length=30)
	age = models.IntegerField()
	# 增加一对一的引用，引用子Ａuthor实体
	author = models.OneToOneField(Author, null=True)
	
	def __str__(self):
		return self.names
	
	class Meta:
		db_table = 'wife'
		verbose_name = '作者夫人'
		verbose_name_plural = verbose_name
