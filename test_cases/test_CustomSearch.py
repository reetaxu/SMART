import unittest
from selenium.webdriver import Firefox


class TestCaseCustomSearch(unittest.TestCase):

    def setUp(self):
        """
        test description:
        setUp
        """
        print('setup')

    def tearDown(self):
        """
        test description:
        tearDown
        """
        print('tearDown')

    def test_test1(self):
        """
        test_test1
        """
        driver = Firefox()
        driver.get('https://www.google.com/')
        print('TestCaseCustomSearch test_test1')

    def test_test2(self):
        """
        test_test2
        """
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
