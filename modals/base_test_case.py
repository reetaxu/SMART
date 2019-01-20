import unittest, time
from selenium import webdriver
from common import settings


class BaseTestCase(unittest.TestCase):

    test_result = 'Pass'

    def setUp(self):
        # self.driver = webdriver.Firefox()
        print('setup')
        # self.driver.get('https://www.baidu.com')

    def tearDown(self):
        time.sleep(2)
        print('teardown')
        print(self.test_result)
        # self.driver.close()