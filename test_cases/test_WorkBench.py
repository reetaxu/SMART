import unittest
from selenium.webdriver import Firefox


# from common.settings2 import Settings2


class TestCaseWorkBench(unittest.TestCase):
    def setUp(self):
        print('setup')
        # print(Settings2.url)

    def tearDown(self):
        print('tearDown')

    def test_test1(self):
        driver = Firefox()
        driver.get('https://www.google.com/')
        print('TestCaseCustomSearch test_test1')

    def test_test2(self):
        driver = Firefox()
        driver.get('https://www.google.com/')
        print('TestCaseCustomSearch test_test2')

    def test_test3(self):
        driver = Firefox()
        driver.get('https://www.google.com/')
        print('TestCaseCustomSearch test_test3')

    def test_test4(self):
        driver = Firefox()
        driver.get('https://www.google.com/')
        print('TestCaseCustomSearch test_test4')


if __name__ == '__main__':
    unittest.main()
