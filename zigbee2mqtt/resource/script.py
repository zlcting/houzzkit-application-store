import sys,json,os,time

# 访问脚本名称
script_name = sys.argv[0]

# 替换文件内容中的占位符
mqttService = sys.argv[1]

# 创建文件并写入内容
#file_name = sys.argv[2]
file_name = "/var/data/zigbee2mqtt/data/configuration.yaml"
script_res = {}
# 定义要写入的字典对象
json_string = '''
{
    "external_converters": [],
    "devices": [
        "devices.yaml"
    ],
    "groups": [
        "groups.yaml"
    ],
    "homeassistant": true,
    "permit_join": false,
    "mqtt": {
        "base_topic": "zigbee2mqtt",
        "server": "|mqtt_service|",
        "user": "mqtt",
        "password": "mqtt",
        "force_disable_retain": false
    },
    "serial": {
        "port": "/dev/ttyUSB0"
    },
    "advanced": {
        "log_level": "warn",
        "pan_id": 6754,
        "channel": 11,
        "network_key": [
            1,
            3,
            5,
            7,
            9,
            11,
            13,
            15,
            0,
            2,
            4,
            6,
            8,
            10,
            12,
            13
        ],
        "availability_blocklist": [],
        "availability_passlist": []
    },
    "device_options": {},
    "blocklist": [],
    "passlist": [],
    "queue": {},
    "frontend": {
        "port": 8099
    },
    "experimental": {}
}
'''
# 使用 replace 方法替换内容
updated_content = json_string.replace("|mqtt_service|", mqttService)
res = {
    "file-text":updated_content,
    "file-path":file_name,
}
script_res = {
    "param_map":res,
    "err":""
}
f = open('/tmp/configuration.yaml', 'w')
# 写入内容到文件
f.write(updated_content)
# 关闭文件
f.close()

time.sleep(2)
json_str = json.dumps(script_res)
print(json_str)