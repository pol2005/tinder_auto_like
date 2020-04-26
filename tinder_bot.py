from selenium import webdriver
from time import sleep

USERNAME = ""
PASSWORD = ""


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()


    def login(self):
        self.driver.get("https://tinder.com")

        cookies_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        cookies_btn.click()

        fb_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        fb_btn.click()

        base_window = self.driver.window_handles[0]
        popup = self.driver.window_handles[1]

        self.driver.switch_to.window(popup)
        email = self.driver.find_element_by_xpath('//*[@id="email"]')
        passwd = self.driver.find_element_by_xpath('//*[@id="pass"]')
        email.send_keys(USERNAME)
        passwd.send_keys(PASSWORD)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to.window(base_window)
        location_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        location_btn.click()

        notification_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        notification_btn.click()

        set_location_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button')
        set_location_btn.click()


    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()


    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()


    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                self.like()
            except Exception:
                self.close_popup()
            finally:
                if self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]'):
                    print("Max likes reached")
                    break
                else:
                    self.close_match()


    def close_popup(self):
        popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()



b = TinderBot()
b.login()
b.auto_swipe()







