#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-3-20 下午2:40
# @Author  : Michael
# @Site    : 
# @File    : urls.py
# @Software: PyCharm

from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
	path('test/',views.test)
]