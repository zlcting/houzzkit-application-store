import json
import requests


class ResLogin:
    def __init__(self):
        self.version = 0
        self.type = ""
        self.flow_id = ""
        self.handler = []
        self.step_id = ""
        self.data_schema = []
        self.errors = ""
        self.description = None
        self.description_placeholders = None
        self.last_step = None
        self.result = ""


def Login(url, username, password, token, client_id, redirect_uri):
    url = url + "/auth/login_flow"
    msg = {}
    if len(token) == 0:
        msg = {
            "client_id": client_id,
            "handler": ["homeassistant", None],
            "redirect_uri": redirect_uri
        }

    if len(token) > 0:
        url = url + "/" + token
        msg = {
            "client_id": client_id,
            "username": username,
            "password": password,
        }
    json_msg = json.dumps(msg)
    headers = {
        'Content-Type': 'text/plain;charset=UTF-8',
    }
    post = mypost(url, json_msg, headers)
    # res = ResLogin()
    json_res = json.loads(post.text)
    # res.type = json_res["type"]
    # res.flow_id = json_res["flow_id"]
    # res.handler = json_res["handler"]
    # res.step_id = json_res["step_id"]
    # res.data_schema = json_res["data_schema"]
    # res.errors = json_res["errors"]
    # res.last_step = json_res["last_step"]
    # res.result = json_res["result"]
    return json_res


def mypost(url, data, headers):
    # 发送POST请求，包括自定义的头部信息
    response = requests.post(url, data=data, headers=headers)

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


def get_token_auth(token, client_id):
    url = "http://127.0.0.1:8123/auth/token"
    msg = {
        "client_id": client_id,
        "code": token,
        "grant_type": "authorization_code"
    }
    # print(msg)
    response = requests.post(url, data=msg)
    
    # return response.text
    # print(response.text)
    return json.loads(response.text)
