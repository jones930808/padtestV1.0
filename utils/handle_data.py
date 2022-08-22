# -*- coding: utf-8 -*-
# @Time : 2022/8/23 0:13
# @Author : JoJoMi学习历险记
# @File : handle_data.py

"""
函数需求：MD5加密操作
入参：加密的明文 --string类型
出参：加密后的密文--string类型
"""
import hashlib


def get_md5_data(pwd:str):
    #1、实例话md5对象
    md5 = hashlib.md5()
    #2、调用加密操作
    md5.update(pwd.encode('utf-8'))
    #3、返回加密后的结果 16进制结果
    return md5.hexdigest()