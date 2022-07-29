import pytest
from example.common.yaml_util import clear_config_yaml,read_yaml_by_key

from example.interface.interface_dashboard import Interface_dashboard
# from example.common.yaml_util import clear_config_yaml
# from example.action.action_explorer import ActioDashboard


"""
    TODO：前置条件的准备：
        配置graph、hdfs以及palto节点的信息
"""


@pytest.fixture(scope="session", autouse=True)
def login():
    clear_config_yaml()
   
#解绑集群
    yield
    Interface_dashboard().interface_unbind(read_yaml_by_key("cluster_id","/conf/temp.yaml"))
    
    

    