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


def check_activation_code(activation_code): 
    url1 = "https://activecode-1-9gyjmiqg675db947-1310894818.ap-shanghai.app.tcloudbase.com/test"  
    payload = {"activation_code": activation_code}  
    headers = {"Content-Type": "application/json"}  
    response = requests.post(url1, json=payload, headers=headers)   
    
    return response.text    