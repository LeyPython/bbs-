"""Mybbs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from bbs import views
from django.conf.urls import url, include
from django.views.static import serve
from django.conf import settings
from stark.service.stark import site
from bbs import urls as bbs_urls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('login/', views.login),  # 登录
    path('pc-geetest/register', views.get_geetest),  # 极验滑动验证码 获取验证码的url
    path('register/', views.register),  # 注册
    path('check_username_exist/', views.check_username_exist),  # 专门用来校验用户名是否已被注册的接口
    re_path('media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),  # media

    path('index/', views.index),  # bbs主页
    path('logout/', views.logout),  # 注销
    path('stark/', site.urls),  # stark组件
    url(r'bbs/', include(bbs_urls)),  # 将所有以bbs开头的url都交给app下面的urls.py来处理
    path('upload/', views.upload),
]


