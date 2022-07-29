import base64
from time import sleep
from example.common.yaml_util import read_yaml_by_key, write_yaml_by_key
from example.interface.interface_dashboard import Interface_dashboard
from example.interface.interface_dashboard import Interface_dashboard


class ActioDashboard(object):
    def action_connect(self):
        # login
        username = read_yaml_by_key("graphd_username")
        password = read_yaml_by_key("graphd_password")
        # graphd_ip = read_yaml_by_key("graphd_ip")
        # graphd_port = read_yaml_by_key("graphd_port")

        login_info = {
            "username": username,
            "password": password,
            # "graphd_ip": graphd_ip,
            # "graphd_port": graphd_port
        }

        Interface_dashboard().interface_connect(login_info)
