from django.db import models

# Create your models here.

class GoodsType(models.Model):
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='static/upload/goodstype')
    desc = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    class Meta:
        #修改表明
        db_table='goodstype'
        #修改展示名字
        verbose_name = '商品类型'
        #复数形式
        verbose_name_plural = verbose_name
       
       

class Goods(models.Model):
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    unit = models.CharField(max_length=20,null=True)
    #spec详细说明
    spec = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='staic/upload/goods')
    isActive = models.BooleanField(default=True)
    #　设置对goodstype的引用(1:M)
    goodsType = models.ForeignKey(GoodsType, null=True)
    
    #修改后台页面中每个对象的名字
    def __str__(self):
        return self.title
    
    #定义类的展示形式
    class Meta:
        #修改表名
        db_table = 'goods'
        #修改后台管理展示名字
        verbose_name = '商品'
        #复数形式
        verbose_name_plural = verbose_name
        #排序规则(价格)
        ordering = ['price']
        
class Users(models.Model):
    uphone = models.CharField(max_length=11)
    upwd = models.CharField(max_length=20)
    uemail = models.EmailField(null=True)
    uname = models.CharField(max_length=20)
    isActive = models.BooleanField(default=True)
    
    #修改后台管理中每个对象的名字
    def __str__(self):
        return self.uname
    
    #定义类的后台展示形式
    class Meta:
        #修改表名
        db_table = 'users'
        #修改后台管理展示名字
        verbose_name = '用户'
        verbose_name_plural = verbose_name
        #用户排序更具id倒序
        ordering = ['-id']
