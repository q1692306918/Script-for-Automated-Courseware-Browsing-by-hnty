import logging
import tkinter as tk
import subprocess

import requests


def setup_logging():
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def update_status_text(status_text, text):  # 将状态信息显示在状态文本框中
    status_text.insert(tk.END, text + "\n") # 将状态信息显示在状态文本框中
    status_text.see(tk.END) # 将滚动条移动到最下方
    logging.info(text)  # 将状态信息记录到日志文件


def check_activation_code(activation_code): # 检查激活码是否有效
    url1 = "https://activecode-1-9gyjmiqg675db947-1310894818.ap-shanghai.app.tcloudbase.com/test"  # 替换为后端激活码验证URL
    payload = {"activation_code": activation_code}  # 构造请求体
    headers = {"Content-Type": "application/json"}  # 构造请求头
    response = requests.post(url1, json=payload, headers=headers)   # 发送请求
    # print(response.json())
    return response.text    # 返回响应体