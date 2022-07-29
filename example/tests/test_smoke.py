from dataclasses import dataclass
from time import sleep
import pytest
from example.common.yaml_util import read_yaml_by_key
from example.interface.interface_dashboard import Interface_dashboard


class TestSmoke():
    nebula_list = [{"ip" : "192.168.8.134", "port" : 9669, "username" : "root", "password" :"123" } ]
    @pytest.mark.smoke
    def test_smoke_login(self):
        # print(1)
        login_info = {
            "username": read_yaml_by_key("username"),
            "password": read_yaml_by_key("password"),
        }
        print("login_info:",login_info)
        login_result = Interface_dashboard().interface_login(
            login_info)
        
        assert login_result.json()["code"] == 0, "预期值不符合"
        
        
    @pytest.mark.smoke
    @pytest.mark.parametrize("nebula_info",nebula_list )
    def test_smoke_account(self,nebula_info):
        Interface_dashboard().interface_account(nebula_info)
    #     print(nebula_info["ip"])
        
    @pytest.mark.smoke
    def test_smoke_approve(self):
        Interface_dashboard().interface_approve()
        
    @pytest.mark.smoke
    def test_smoke_import(self):
        Interface_dashboard().interface_import()
        sleep(2) 
       
    @pytest.mark.smoke
    def test_smoke_clusters(self):
        Interface_dashboard().interface_clusters()
    