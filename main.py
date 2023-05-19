import threading
import time
import easygui
from browser import browser_handless_edge, close_app
from handlers import handle_mp4, handle_ptx
from gui import create_root_window, get_activation_code, get_url
from utils import update_status_text, check_activation_code, submit, getUser


def main(driver, root, status_text, exit_button, user_status):
    user = getUser(url, driver)

    exit_thread = threading.Event()
    driver.get(url)
    driver.implicitly_wait(10)
    exit_button.config(command=lambda: close_app(driver, root, exit_thread))

    while not exit_thread.is_set():
        try:
            divs = driver.find_elements_by_css_selector('._1QoJyBnLPXjLp8cV61PPJe')
            for div in divs:
                name = div.find_element_by_css_selector('._3dYlgmbXq9p-8xwwf_goNT').text
                class_ = name.split('-')[1]
                if user_status != 'ERROR: user already exists':
                    print(user_status)
                    user_status = submit(user, class_, user_status)
                status = div.find_element_by_css_selector('._3HzEldvxtmCRMKy_ELaND8 :nth-child(2)').text[-1]
                status1 = div.find_element_by_css_selector('._3HzEldvxtmCRMKy_ELaND8 :nth-child(2)').text[-2]
                update_status_text(status_text, f'未读{status}')

                if status == '0' and status1 != '1' and status1 != '2':
                    update_status_text(status_text, f'{name}已完成！')
                    continue
                update_status_text(status_text, f'{name}开始')
                div.click()
                break

            while True:
                card = driver.find_element_by_css_selector('._1UfYCzyzkv94Zbsyr_Hoc0')
                update_status_text(status_text, card.text)
                status = card.find_element_by_css_selector('._1GoZ9bt9hJQ5yLFgOgeVOI').text
                update_status_text(status_text, status)

                if status == '已读':
                    update_status_text(status_text, '全部已完成')
                    driver.get(url)
                    break

                type_work = card.find_element_by_css_selector('.dPphweSVDC1Hf6EnOO71w').text[-3:]
                update_status_text(status_text, type_work)
                card.click()
                time.sleep(0.5)
                driver.find_element_by_css_selector('.weui-actionsheet__cell').click()

                if type_work == 'mp4':
                    handle_mp4(driver, status_text)
                elif type_work == 'ptx':
                    handle_ptx(driver, status_text)

                time.sleep(60)
                driver.find_element_by_css_selector('._3IXHvJLszKa_-s4kn1kPlT').click()
                driver.refresh()
                time.sleep(3)
            root.update()
        except:
            if exit_thread.is_set():
                break
            driver.save_screenshot('结果.png')
            update_status_text(status_text, '出了点问题')
            main(driver, root, status_text, exit_button, user_status)


if __name__ == "__main__":
    while True:
        activation_code = get_activation_code()
        print(check_activation_code(activation_code))
        if check_activation_code(activation_code) == "SUCCESS":
            easygui.msgbox("本次激活成功！")
            break
        else:
            easygui.msgbox(check_activation_code(activation_code))
    user_status = ''
    driver = browser_handless_edge()
    url = get_url()
    root, status_text, exit_button = create_root_window()
    update_status_text(status_text, "Program start")

    thread = threading.Thread(target=main, args=(driver, root, status_text, exit_button, user_status))
    thread.start()

    root.mainloop()
