from django import forms
from .models import *

# 为topic下拉列表初始化一组数据，　－　元祖
# - > <option value='level1'>好评</option>
TOPIC_CHOICE = (
	('level1', '好评'),
	('level1', '中评'),
	('level1', '好评'),
)


class RemarkForm(forms.Form):
	# 1.创建subject属性,表示评论标题,显示成文本框
	# 1.１lobel生成的控件前面的提示文本
	# 1.2inital表示初始化的数据，等同于控件value
	subject = forms.CharField(label='标题', initial='初始数据')
	# 2.创建email属性,表示邮箱,小城成email控件
	# 2.1label表示初始化钱
	email = forms.EmailField(label="邮箱")
	# 3.创建一个message属性,表示评论内容,显示成多行文本域
	message = forms.CharField(label='内容', widget=forms.Textarea)
	# 4.创建要给topic属性，表示评论级别,显示成一个下拉列表
	# choices指定下拉列表选项的数据们
	topic = forms.ChoiceField(label='评价', choices=TOPIC_CHOICE)
	# ５.创建isSave属性，表示是否保存，显示一个复选狂
	isSave = forms.BooleanField(label='是否保存')


class RegisterForm(forms.Form):
	uname = forms.CharField(label='用户名称')
	upwd = forms.CharField(label='用户密码', widget=forms.PasswordInput)
	uemail = forms.EmailField(label='电子邮箱')
	uage = forms.IntegerField(label='年龄')


class LoginForm(forms.ModelForm):
	# 创建内部类Meta
	class Meta:
		# 关联的Models
		model = Users()
		# 定义要生成控件的属性们
		# fields = "__all__"
		fields = ['uname', 'upwd']
		# 每个控件对应的label
		labels = {
			"uname": "用户名称",
			"upwd": "用户密码",
		}
