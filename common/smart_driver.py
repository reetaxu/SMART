from selenium import webdriver
from tools import common_tools


class SmartDriver(webdriver.Firefox):

    # def __init__(self):
    #     common_tools.save_log('open browser : Firefox')
    #     return self.__init__()

    def find_element_(self, by, value):
        str_ = 'Find Element by:{0}, value:{1}'.format(by, value)
        common_tools.save_log(str_)
        return self.find_element(by, value)

    def find_elements_(self, by, value):
        str_ = 'Find Elements by:{0}, value:{1}'.format(by, value)
        common_tools.save_log(str_)
        return self.find_elements(by, value)
