import json
import requests
import time

def node_red_config(token):
    url = 'http://127.0.0.1:8123/api/config/config_entries/flow'
    token = "Bearer "+token
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': token
    }
    data = {
        'handler': 'nodered',
        'show_advanced_options': False
    }
    response = requests.post(url, headers=headers, json=data)
    #print(response.text)

    response_text = json.loads(response.text)
    
    url = url + "/" + response_text["flow_id"]
    
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'authorization': token
    }
    data = {}

    response = requests.post(url, headers=headers, json=data)
    response_text = json.loads(response.text)
    # todo 需要更新sqlite 中的集成表中的entry_id 字段
    # print("集成id：",response_text["result"]["entry_id"])
    # print("集成id：",response_text)



def check_connection():
    url = f"http://127.0.0.1:8123"
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


is_reachable = check_connection()
# if is_reachable:
#     print(f"地址可联通!")
# else:
#     print(f"地址不可联通.")