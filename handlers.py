import time

from utils import update_status_text


def handle_mp4(driver, status_text):
    time.sleep(5)
    driver.find_element_by_css_selector('.outter').click()  # 点击播放
    update_status_text(status_text, "现在还在iframe")   # 更新状态栏
    mp4_status = True   # mp4状态
    while mp4_status:   # mp4状态为真
        tm1 = driver.find_element_by_css_selector('.current-time').text # 当前时间
        tm2 = driver.find_element_by_css_selector('.duration').text # 总时间
        print(tm1)  # 打印当前时间
        if tm1 == tm2 and tm1 != '00:00':   # 如果当前时间等于总时间且不等于00:00
            print(tm1, tm2) # 打印当前时间和总时间
            mp4_status = False  # mp4状态为假
            break   # 跳出循环
    driver.switch_to.parent_frame() # 切换到父级iframe
    driver.switch_to.default_content()  # 切换到默认iframe
    update_status_text(status_text, '回到default_content')    # 更新状态栏


def handle_ptx(driver, status_text):    # 处理ptx
    iframe = driver.find_element_by_css_selector('._1a4S0yFBO4gZoRFvUkRkW6')    # 定位iframe
    driver.switch_to.frame(iframe)  # 切换到iframe
    time.sleep(5)
    while True: # 循环
        index = driver.find_element_by_xpath('//*[@id="PageIndex"]').text
        max_index = driver.find_element_by_xpath('//*[@id="PageCount"]').text   #获取当前页和总页
        update_status_text(status_text, f'index:{index} max:{max_index}')   # 更新状态栏
        driver.find_element_by_css_selector('.btm .btmRight').click()   # 点击下一页
        time.sleep(0.5)
        if index == max_index:  # 如果当前页等于总页
            for i in range(10): # 循环10次
                driver.find_element_by_css_selector('.btm .btmRight').click()   # 点击下一页
            time.sleep(60)  # 等待60秒
            update_status_text(status_text, '现在还在iframe')   # 更新状态栏
            driver.switch_to.parent_frame() # 切换到父级iframe
            driver.switch_to.default_content()  # 切换到默认iframe
            update_status_text(status_text, '回到default_content')    # 更新状态栏
            break
