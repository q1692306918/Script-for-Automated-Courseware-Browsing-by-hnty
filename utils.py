import logging
import tkinter as tk
import subprocess

import requests


def setup_logging():
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def update_status_text(status_text, text):  
    status_text.insert(tk.END, text + "\n") 
    status_text.see(tk.END) 
    logging.info(text)  

def getUser(url,driver):
    openID =url[url.rfind('=') + 1:]
    print(openID)
    homepage = f'http://www.hntyxxh.com/wechat2-ssr/?openid={openID}&from=wzj'
    print(homepage)
    driver.get(homepage)
    user = driver.find_element_by_css_selector('.EXQcJu5rkwcRFryNNYIQV').text
    return user


def submit(user,class_,user_status):
    url = 'https://activecode-1-9gyjmiqg675db947-1310894818.ap-shanghai.app.tcloudbase.com/user_info'
    data = {'user': user, 'class': class_}
    response = requests.get(url, json=data)
    print(response.text)
    user_status=response.text
    return user_status
def check_activation_code(activation_code): 
    url1 = "https://activecode-1-9gyjmiqg675db947-1310894818.ap-shanghai.app.tcloudbase.com/test"  
    payload = {"activation_code": activation_code}  
    headers = {"Content-Type": "application/json"}  
    response = requests.post(url1, json=payload, headers=headers)   
    
    return response.text    