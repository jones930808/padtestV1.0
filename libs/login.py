# -*- coding: utf-8 -*-
# @Time : 2022/8/22 23:33
# @Author : JoJoMi学习历险记
# @File : login.py

"""
封装代码： 使用函数，还是类？
类：封装、继承、多态
"""
from configs.config import HOST
import requests
from utils.handle_data import get_md5_data


# 封装登录类
class Login:
    # 封装登录接口
    def login(self, body_data):
        # 1、请求url拼接
        url = f'{HOST}/api/loginS'
        # 2、请求头
        # 3、请求体
        body_data['password'] = get_md5_data(body_data['password'])
        payload = body_data
        #4、发送请求
        resp = requests.post(url, json=payload )
        #5、打印响应数据
        return resp.text

    # def logout(self):
    #     pass

if __name__ == '__main__':
    test_data= {"username":"","password":"123456"}
    #1、使用类去创建实例
    login = Login()
    #2、Login()括号中有__new__(self);__init__(self)
    res = login.login(test_data)