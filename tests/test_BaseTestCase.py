from modals import base_test_case
import unittest
from selenium import webdriver


class BaseTC(base_test_case.BaseTestCase):
    qa_name = 'Jon'

    def test_test1(self):
        print(self.test_result)
        self.test_result = 'Fail'


if __name__ == '__main__':
    unittest.main()

# class BaseTC2(base_test_case.BaseTestCase2):
#     def __init__(self):
#         base_test_case.BaseTestCase2.__init__(qa_name='')
#
#     def test_test1(self):
#         print(self.test_result)
#
#
# if __name__ == '__main__':
#     unittest.main()

# class TestCase(unittest.TestCase):
#     def test_BaseTestCase(self):
#         test_case1 = BaseTC(driver=webdriver.Firefox(), qa_name='Jon', test_result='Pass')
