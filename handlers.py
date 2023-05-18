import time

from utils import update_status_text


def handle_mp4(driver, status_text):
    time.sleep(5)
    driver.find_element_by_css_selector('.outter').click()  
    update_status_text(status_text, "现在还在iframe")   
    mp4_status = True   
    while mp4_status:   
        tm1 = driver.find_element_by_css_selector('.current-time').text 
        tm2 = driver.find_element_by_css_selector('.duration').text 
        print(tm1)  
        if tm1 == tm2 and tm1 != '00:00':   
            print(tm1, tm2) 
            mp4_status = False  
            break   
    driver.switch_to.parent_frame() 
    driver.switch_to.default_content()  
    update_status_text(status_text, '回到default_content')    


def handle_ptx(driver, status_text):    
    iframe = driver.find_element_by_css_selector('._1a4S0yFBO4gZoRFvUkRkW6')    
    driver.switch_to.frame(iframe)  
    time.sleep(5)
    while True: 
        index = driver.find_element_by_xpath('//*[@id="PageIndex"]').text
        max_index = driver.find_element_by_xpath('//*[@id="PageCount"]').text   
        update_status_text(status_text, f'index:{index} max:{max_index}')   
        driver.find_element_by_css_selector('.btm .btmRight').click()   
        time.sleep(0.5)
        if index == max_index:  
            for i in range(10): 
                driver.find_element_by_css_selector('.btm .btmRight').click()   
            time.sleep(60)  
            update_status_text(status_text, '现在还在iframe')   
            driver.switch_to.parent_frame() 
            driver.switch_to.default_content()  
            update_status_text(status_text, '回到default_content')    
            break
