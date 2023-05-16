import tkinter as tk
from tkinter import ttk
import easygui

from browser import close_app


def create_root_window():   # 创建窗口对象的背景色
    root = tk.Tk()  #中文注释   # 创建窗口对象的背景色
    root.title("精华平台课件自动化，作者微信:q1692306918")    # 设置窗口标题
    root.config(bg="white") # 创建窗口对象的背景色

    frame = ttk.Frame(root)     # 创建一个容器
    frame.pack(fill=tk.BOTH, expand=True)   # 创建一个容器

    status_text = tk.Text(frame, wrap=tk.WORD, font=13)  # 创建一个文本框，设置它的字体为13号字，设置文本换行
    status_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)   # 将文本框填充满整个窗口

    scrollbar = ttk.Scrollbar(frame, command=status_text.yview) # 创建一个滚动条，设置与文本框关联
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)    # 将滚动条填充满整个窗口

    status_text.configure(yscrollcommand=scrollbar.set)   # 将滚动条与文本框关联

    exit_button_frame = ttk.Frame(root)  # Create a frame for the button
    exit_button_frame.pack(side=tk.BOTTOM, pady=10)  # Put the frame at the bottom of the window

    exit_button = ttk.Button(exit_button_frame, text="Exit", command=close_app)  # Create the button
    exit_button.pack()  # Put the button in the frame

    return root, status_text, exit_button   # 返回窗口对象


def get_activation_code():
    while True:
        activation_code = easygui.enterbox("联系微信q1692306918获取激活码" + "\n" + "请输入激活码：",
                                           title="精华平台一键通")
        if activation_code:
            return activation_code


def get_url():  # 获取用户输入的链接
    return easygui.enterbox("请输入您的链接：", default="https://") # 获取用户输入的链接
