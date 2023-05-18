import subprocess
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from msedge.selenium_tools import EdgeOptions, Edge


def browser_handless_edge():
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("--mute-audio") 
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('window-size=1920x1080')
    options.add_argument('--start-maximized')
    options.add_argument("--disable-blink-features=AutomationControlled")  
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')

    
    path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    options.binary_location = path

    browser = Edge(options=options) 
    return browser  


def browser_handless(): 
    options = ChromeOptions()   
    options.add_argument("--mute-audio")  
    options.add_argument('--headless')  
    options.add_argument('--disable-gpu')   
    options.add_argument('window-size=1920x1080')   
    options.add_argument('--start-maximized')   
    options.add_argument("--disable-blink-features=AutomationControlled")   
    options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36')

    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    options.binary_location = path
    browser = webdriver.Chrome(chrome_options=options)
    return browser  


def close_app(driver, root, exit_thread):   
    exit_thread.set()  
    driver.quit()   
    
    subprocess.call(['taskkill', '/f', '/im', 'chrome.exe'])    
    subprocess.call(['taskkill', '/f', '/im', 'chromedriver.exe'])
    subprocess.call(['taskkill', '/f', '/im', 'msedge.exe'])
    root.destroy()  
