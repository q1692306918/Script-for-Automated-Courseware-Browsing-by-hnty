import threading
import time

import easygui
from browser import browser_handless_edge, close_app
from handlers import handle_mp4, handle_ptx
from gui import create_root_window, get_activation_code, get_url
from utils import update_status_text, check_activation_code


def main(driver, root, status_text, exit_button):
    exit_thread = threading.Event()  # 创建一个事件对象
    driver.get(url) # 打开网页
    driver.implicitly_wait(10)  # 隐式等待10秒

    exit_button.config(command=lambda: close_app(driver, root, exit_thread))  # 为按钮绑定事件

    while not exit_thread.is_set(): # 当事件未被设置时，循环执行
        try:
            divs = driver.find_elements_by_css_selector('._1QoJyBnLPXjLp8cV61PPJe') # 获取所有的div
            for div in divs:    # 遍历div
                name = div.find_element_by_css_selector('._3dYlgmbXq9p-8xwwf_goNT').text    # 获取div中的标题
                status = div.find_element_by_css_selector('._3HzEldvxtmCRMKy_ELaND8 :nth-child(2)').text[-1]    # 获取div中的状态
                status1 = div.find_element_by_css_selector('._3HzEldvxtmCRMKy_ELaND8 :nth-child(2)').text[-2]   # 获取div中的状态
                update_status_text(status_text, f'未读{status}')  # 更新状态栏

                if status == '0' and status1 != '1' and status1 != '2': # 如果状态为0，且状态1不为1或2，则跳过
                    update_status_text(status_text, f'{name}已完成！')  # 更新状态栏
                    continue    # 跳过
                update_status_text(status_text, f'{name}开始')    # 更新状态栏
                div.click() # 点击div
                break   # 跳出循环
            while True: # 循环执行
                card = driver.find_element_by_css_selector('._1UfYCzyzkv94Zbsyr_Hoc0')  # 获取卡片
                update_status_text(status_text, card.text)  # 更新状态栏
                status = card.find_element_by_css_selector('._1GoZ9bt9hJQ5yLFgOgeVOI').text # 获取状态
                update_status_text(status_text, status) # 更新状态栏

                if status == '已读':  # 如果状态为已读，则跳过
                    update_status_text(status_text, '全部已完成')    # 更新状态栏
                    driver.get(url) # 打开网页
                    break   # 跳出循环

                type_work = card.find_element_by_css_selector('.dPphweSVDC1Hf6EnOO71w').text[-3:]   # 获取类型
                update_status_text(status_text, type_work)  # 更新状态栏
                card.click()    # 点击卡片
                time.sleep(0.5) # 等待0.5秒
                driver.find_element_by_css_selector('.weui-actionsheet__cell').click()  # 点击开始按钮

                if type_work == 'mp4':  # 如果类型为mp4，则调用mp4处理函数
                    handle_mp4(driver, status_text) # 调用mp4处理函数
                elif type_work == 'ptx':    # 如果类型为ptx，则调用ptx处理函数
                    handle_ptx(driver, status_text) # 调用ptx处理函数

                time.sleep(60)
                driver.find_element_by_css_selector('._3IXHvJLszKa_-s4kn1kPlT').click() # 点击完成按钮
                driver.refresh()    # 刷新网页
                time.sleep(3)   # 等待3秒
            root.update()
        except: # 如果出现异常，则跳过
            if exit_thread.is_set():  # 如果事件被设置了，就退出循环
                break   # 跳出循环
            driver.save_screenshot('结果.png')    # 截图
            update_status_text(status_text, '出了点问题')    # 更新状态栏
            main(driver, root, status_text, exit_button)    # 重新调用main函数


if __name__ == "__main__":
    while True: # 循环执行
        activation_code = get_activation_code() # 获取激活码
        print(check_activation_code(activation_code))
        if check_activation_code(activation_code) == "SUCCESS": # 如果激活码正确，则跳出循环
            easygui.msgbox("本次激活成功！")   # 弹出消息框
            break   # 跳出循环
        else:
            easygui.msgbox(check_activation_code(activation_code))  # 弹出消息框

    driver = browser_handless_edge()    # 创建浏览器对象
    url = get_url() # 获取网址
    root, status_text, exit_button = create_root_window()   # 创建窗口
    update_status_text(status_text, "Program start")    # 更新状态栏

    thread = threading.Thread(target=main, args=(driver, root, status_text, exit_button))   # 创建线程
    thread.start()  # 启动线程

    root.mainloop() # 进入消息循环
