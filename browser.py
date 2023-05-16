import subprocess
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from msedge.selenium_tools import EdgeOptions, Edge


def browser_handless_edge():
    options = EdgeOptions() # 创建EdgeOptions对象
    options.use_chromium = True  # 使用Chromium内核
    options.add_argument("--mute-audio")  # 静音
    options.add_argument('--headless')  # 无头模式
    options.add_argument('--disable-gpu')   # 禁用GPU加速
    options.add_argument('window-size=1920x1080')   # 设置窗口大小
    options.add_argument('--start-maximized')   # 最大化窗口
    options.add_argument("--disable-blink-features=AutomationControlled")  # 禁用自动化控制
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')

    # 设置Edge浏览器的路径
    path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    options.binary_location = path

    browser = Edge(options=options) # 创建Edge对象
    return browser  # 返回Edge对象


def browser_handless(): # 创建无头Chrome浏览器
    options = ChromeOptions()   # 创建ChromeOptions对象
    options.add_argument("--mute-audio")  # 静音
    options.add_argument('--headless')  # 无头模式
    options.add_argument('--disable-gpu')   # 禁用GPU加速
    options.add_argument('window-size=1920x1080')   # 设置窗口大小
    options.add_argument('--start-maximized')   # 最大化窗口
    options.add_argument("--disable-blink-features=AutomationControlled")   # 禁用自动化控制
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')

    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    options.binary_location = path
    browser = webdriver.Chrome(chrome_options=options)
    return browser  # 返回Chrome对象


def close_app(driver, root, exit_thread):   # 关闭应用
    exit_thread.set()  # 设置退出线程标志,防止线程问题引发的webDriver会话问题，主线程逻辑紊乱等异常
    driver.quit()   # 退出webDriver
    # webDriver在quit/close后会残留进程，引用命令行kill
    subprocess.call(['taskkill', '/f', '/im', 'chrome.exe'])    # 引用命令行kill
    subprocess.call(['taskkill', '/f', '/im', 'chromedriver.exe'])
    subprocess.call(['taskkill', '/f', '/im', 'msedge.exe'])
    root.destroy()  # 销毁应用
