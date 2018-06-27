# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 09:36
# @Author  : jt

import requests
import json
import readConfig as readConfig
localReadConfig = readConfig.ReadConfig()

class testlogin_001():
    # sp公共登陆组件
    def test_login_001(self, token):
        params = {'mobilePhone': '15074980908', 'password': '123456', 'remember': 'true', 'siteName': 'main'}
        url = localReadConfig.get_http('url')

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(headers)
        # r1 = requests.post(url, data=json.dumps(params), headers=headers).text
        # print('新增成功')
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        print(token_act)
        s = json.loads(token_act.text)
        values = s["data"]["access_token"]
        return values

    # admin公共登陆组件
    def test_adminlogin(self, token):
        params = {'mobilePhone': '15000000000', 'password': '123456', 'remember': 'true', 'siteName': 'main'}
        url = "http://admin.ejw.cn/api/login"

        headers = {
            'Content-Type': 'application/json;charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:59.0) Gecko/20100101 Firefox/59.0',
            'Accept - Encoding': 'gzip, deflate',
            'Accept - Language': 'zh - CN, zh;q = 0.9',
            'Referer': 'http://www1.ejw.cn/auth/?backUrl=http%3A%2F%2Fadmin.ejw.cn%2F%23%2F',
            'X-Requested-With': 'XMLHttpRequest'
        }
        print(headers)
        # r1 = requests.post(url, data=json.dumps(params), headers=headers).text
        # print('新增成功')
        token_act = requests.post(url, data=json.dumps(params), headers=headers)
        print(token_act)
        s = json.loads(token_act.text)
        values = s["data"]["access_token"]
        return values