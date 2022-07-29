
from dataclasses import dataclass
from email import header
import json
from nturl2path import url2pathname
import re
from wsgiref import headers

from numpy import True_
from example.common.request_util import RequestMain
from example.common.yaml_util import read_yaml_by_key, write_yaml_by_key
import random
class Interface_dashboard(object):
    token = ""
    def interface_login(self, login_info, default_assert=True):
        print("登录接口")
        url = '/api/v1/account/login'

        headers = {
            'Content-Type': 'application/json;'
        }
        # data
        data = {
            "username": login_info["username"],
            "password": login_info["password"]
        }

        # send request
        data = json.dumps(data)
        result = RequestMain().request_main(method="post", url=url, headers=headers,
                                            data=data, default_assert=default_assert)
        # extract token
        Interface_dashboard.token = result.json()["data"]["token"]
        return result
   
    def interface_account(self, import_info, default_assert=True):
        print("导入集群")
        url = '/api/v1/nebula/connect'

        headers ={
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(Interface_dashboard.token)
        }

        data = {
            "address": import_info["ip"],
            "port": import_info["port"],
            "username": import_info["username"],
            "password": import_info["password"]

        }
        

        # send request
        data= json.dumps(data)
        result = RequestMain().request_main(method="post", url=url, headers=headers,
                                            data=data, default_assert=default_assert) 
        return result
    
    def interface_approve(self, default_assert=True):
        print("授权")
        url = '/api/v1/machines/approve'
        
        headers = {
            
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(Interface_dashboard.token)

        }
        
        data = {
            "machines":[{"host":"192.168.8.69","sshUser":"vesoft","sshPort":22,"sshPwd":"nebula"}]
            
        }
        # send request
        data = json.dumps(data)
        result = RequestMain().request_main(method="post", url=url, headers=headers,
                                            data=data, default_assert=default_assert)
        return result
        
    def interface_import(self, default_assert=True):
        print("导入集群")
        url = '/api/v1/clusters/import'
        
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer {}".format(Interface_dashboard.token)

        }
        
        data = {
            "name":"69","version":"v3.2.0","nebulaType":"community","machines":[{"host":"192.168.8.69","sshUser":"vesoft","sshPort":22,"sshPwd":"nebula","cpu":4,"memory":16.27,"disk":52.43,"sudo":True}],"graphd":[{"host":"192.168.8.69","port":9669}],"metad":[{"host":"192.168.8.69","port":9559}],"storaged":[{"host":"192.168.8.69","port":9779}]
        }
        
         # send request
        data = json.dumps(data)
        result = RequestMain().request_main(method="post", url=url, headers=headers,
                                            data=data, default_assert=default_assert)
        return result
    
    def interface_unbind(self,cluster_id, default_assert=True):
        print("集群解绑")
        url = '/api/v1/clusters/{}/unbind'.format(cluster_id)
        
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer {}".format(Interface_dashboard.token)
        }
    
        
        # # send request
        # data = json.dumps(data)
        result = RequestMain().request_main(method="post", url=url, headers=headers,
                                             default_assert=default_assert)
        return result
    
    def interface_clusters(self, default_assert=True):
        print("获取集群ID")
        url = '/api/v1/clusters'
        
        headers = {
            "Content-Type": "application/json; charset=utf-8",
            "Authorization": "Bearer {}".format(Interface_dashboard.token) 
        }
        result = RequestMain().request_main(method="get", url=url, headers=headers,
                                           default_assert=default_assert)
        
        cluster_id = result.json()["data"][-1]["id"]
        info = {
            "cluster_id": cluster_id
        }
        write_yaml_by_key(info, "/conf/temp.yaml")
        return result