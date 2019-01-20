from selenium import webdriver
from common import settings
from selenium.webdriver.common.by import By


class Login(object):

    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password

    def login(self):
        self.driver.get(settings.url)
        login_ele = self.driver.find_element_(By.ID, 'txtLoginid')
        login_ele.send_keys(self.username)
        password_ele = self.driver.find_element_(By.ID, 'txtPassword')
        password_ele.send_keys(self.password)
        login_ele_btn = self.driver.find_element_(By.ID, 'btnloginText')
        login_ele_btn.click()
