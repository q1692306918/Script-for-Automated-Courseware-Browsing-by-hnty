import tkinter as tk
from tkinter import ttk
import easygui

from browser import close_app


def create_root_window():   
    root = tk.Tk()  
    root.title("精华平台课件自动化，作者微信:q1692306918")    
    root.config(bg="white") 

    frame = ttk.Frame(root)     
    frame.pack(fill=tk.BOTH, expand=True)   

    status_text = tk.Text(frame, wrap=tk.WORD, font=13)  
    status_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)   

    scrollbar = ttk.Scrollbar(frame, command=status_text.yview) 
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)    

    status_text.configure(yscrollcommand=scrollbar.set)   

    exit_button_frame = ttk.Frame(root)  
    exit_button_frame.pack(side=tk.BOTTOM, pady=10)  

    exit_button = ttk.Button(exit_button_frame, text="Exit", command=close_app)  
    exit_button.pack()  

    return root, status_text, exit_button   


def get_activation_code():
    while True:
        activation_code = easygui.enterbox("联系微信q1692306918获取激活码" + "\n" + "请输入激活码：",
                                           title="精华平台一键通")
        if activation_code:
            return activation_code


def get_url():  
    return easygui.enterbox("请输入您的链接：", default="https://") 
