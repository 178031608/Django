from django.conf.urls import url
from .views import *

urlpatterns = [
	url(r'^01_request/$', request_views),
]