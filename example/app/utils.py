#!usr/bin/env python 
# -*- coding:utf-8 _*-
"""
@author:ivan
@file: utils.py 
@version:
@time: 2019/05/22 
@email:chongwuwy@163.com
"""


def set_attr(span, request):
    """
    自定义追踪服务需要的参数
    :param span:
    :param request:
    :return:
    """
    span.add_attribute('django.my.test', 'this is a success message!')
    span.add_attribute('996', 'fuck you!')

