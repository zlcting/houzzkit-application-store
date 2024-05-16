import sys,json,os,requests,subprocess,time
s = os.path.abspath(__file__)
sys.path.append(os.path.dirname(s)+'/hass')
import ws
import hassconfig

from urllib.parse import urljoin

from login import Login
from login import get_token_auth
from datetime import datetime

def check_connection():
    url = f"http://127.0.0.1:1880"
    timeout = 60  # 请求超时时间为5秒
    total_time = 300  # 总共运行时间为300秒（5分钟）
    start_time = time.time()  # 记录开始时间

    while time.time() - start_time < total_time:
        try:
            response = requests.get(url, timeout=timeout)
            if response.status_code == 200:
                time.sleep(30)  # 休眠10秒继续下一次判断
                return True  # 地址可联通

        except (requests.exceptions.RequestException, requests.exceptions.Timeout):
            pass  # 忽略连接错误或超时错误

        time.sleep(10)  # 休眠10秒继续下一次判断

    return False  # 超时，地址不可联通

def execute_npm_command_in_docker_container(container_id):
    docker_command = f"docker exec {container_id} npm config set registry https://registry.npmmirror.com"
    subprocess.call(docker_command, shell=True)

# python3 node_red.py zlc 123 http://127.0.0.1:8123
def install_ws_extends():
    url = "http://127.0.0.1:1880/nodes"
    data = {
        "module":"node-red-contrib-home-assistant-websocket",
        "version":"0.59.0"
    }
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Node-RED-API-Version': 'v2'
    }
    # 发送POST请求，包括自定义的头部信息
    response = requests.post(url, json=data, headers=headers)

    # 检查响应状态码
    # if response.status_code == 200:
    #     # 请求成功
    #     print("访问成功！")
    # else:
    #     # 请求失败
    #     print("访问失败！")
    # print(response.text)
    # 打印响应内容
    return response
def config_node_hass_token(token):
    url = "http://127.0.0.1:1880/flows"
    headers = {
        'Node-RED-API-Version': 'v2'
    }
    response = requests.get(url, headers=headers)
    res_data = json.loads(response.text)
    rev = res_data["rev"]
    # 获取当前机器的ip地址    
    data = {
    "flows": [
        {
            "id": "9507117b9a90ec08",
            "type": "server",
            "name": "Home Assistant",
            "version": 5,
            "addon": False,
            "rejectUnauthorizedCerts": False,
            "ha_boolean": "y|yes|true|on|home|open",
            "connectionDelay": True,
            "cacheJson": True,
            "heartbeat": False,
            "heartbeatInterval": "30",
            "areaSelector": "friendlyName",
            "deviceSelector": "friendlyName",
            "entitySelector": "friendlyName",
            "statusSeparator": ": ",
            "statusYear": "hidden",
            "statusMonth": "short",
            "statusDay": "numeric",
            "statusHourCycle": "default",
            "statusTimeFormat": "h:m",
            "enableGlobalContextStore": False,
            "credentials": {
                "host": "http://192.168.55.1:8123",
                "access_token": token
            }
        }
    ],
    "rev": rev
    }
    response =requests.post(url,json=data,headers=headers)
    #     # 检查响应状态码
    # if response.status_code == 200:
    #     # 请求成功
    #     print("访问成功！",url)
    # else:
    #     # 请求失败
    #     print("访问失败！",url)
    return


# 访问脚本名称
script_name = sys.argv[0]
long_token_info = sys.argv[1]
ipaddress = "http://127.0.0.1:8123"
client_id = "http://127.0.0.1:8123/" 
redirect_uri = "http://127.0.0.1:8123/?auth_callback=1"

is_reachable = hassconfig.check_connection()
if is_reachable:
    hassconfig.node_red_config(long_token_info)
###以下为node red 插件安装
install_ws_extends()
config_node_hass_token(long_token_info)
option = {
"context":"配置完成",
"err":"",
}
json_str = json.dumps(option)
print(json_str)