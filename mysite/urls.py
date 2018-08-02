"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
import quickstart.views as views
from . import settings
from rest_framework.documentation import  include_docs_urls

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url('', include('quickstart.urls')),
    # url(r'^', include(router.urls)),
    url('api-auth/',include('rest_framework.urls')), #登錄api
    url('docs/',include_docs_urls(title='apis'))
]


urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)