#!/bin/bash
param1=$1
# 获取当前shell脚本的路径
script_dir="$(dirname "$0")"
script_py="script.py"
path="${script_dir}/${script_py}"
python3 "$path" "$param1"