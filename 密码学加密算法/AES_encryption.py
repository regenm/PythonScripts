#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @author: A.L.Kun
# @file : test.py
# @time : 2022/4/25 6:22
import binascii  # 进行进制的转换
from Crypto.Cipher import DES  # 导入DES模块
from Crypto import Random  # 进行随机的偏移量


# 加密函数
def encryption(key, iv, data):
    """
    :param key:加密密钥，8位数据
    :param iv: 偏移量，Only applicable for ``MODE_CBC``, ``MODE_CFB``, ``MODE_OFB``,
            and ``MODE_OPENPGP`` modes，并且长度必须为8
    :param data: 要加密的数据
    :return: 返回密文
    """
    cipher = DES.new(key, DES.MODE_CFB, iv)  # 创建加密对象，以及加密规则
    data = cipher.encrypt(data.encode())  # 对数据进行编码后进行加密
    return binascii.b2a_hex(data)  # 得到加密后的16进制数据


# 解密函数
def decryption(key, iv, data):
    """DES解密函数"""
    data = binascii.a2b_hex(data)  # 把十六进制的密文数据转换成二进制数据
    decipher = DES.new(key, DES.MODE_CFB, iv)  # 创建相同的解密规则
    return decipher.decrypt(data).decode()  # 进行解码


keys = b"maqudong"  # 密钥
iv = Random.new().read(8)  # 随机偏移量

data = "一寸相思千万绪，人间每个安排处"

ret = encryption(keys, iv, data)
print(ret)
r_ret = decryption(keys, iv, ret)
print(r_ret)
