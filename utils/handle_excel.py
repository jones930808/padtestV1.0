# -*- coding: utf-8 -*-
# @Time : 2022/8/23 0:36
# @Author : JoJoMi学习历险记
# @File : handle_excel.py

import xlrd

"""
功能需求：获取excel文件的指定数据
入参：
    - 文件路径（路径+文件名+文件格式）
    - 读取指定的sheet表
    - 读取指定单元格数据
出参：函数使用者需要什么类型
    - 返回数据是什么
        - 请求体
        - 预期相应结果
        - 描述
    - 数据的类型
        - 元组
        - 字典
        - 字符串
        - 列表
        - 集合
"""
def get_excel_data(file_path, sheet_name):
    #1、文件在磁盘 ---读取到内存
    #formatting_info = True---保存原样式
    work_book = xlrd.open_workbook(file_path, formatting_info=True)
    #获取所有的sheet名
