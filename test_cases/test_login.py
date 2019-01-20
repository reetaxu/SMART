import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUp(self):
        print('setup')
        self.url = 'http://strzw058051/SMARTSolutions/'
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        print('Activate Firefox, open url: ' + self.url)

    @classmethod
    def tearDown(self):
        print('tearDown')
        print('Collect test result: pass')
        self.driver.quit()
        print('Test case ended, close Firefox')

    def test_succeed(self):
        """
        http://strzw058051/SMARTSolutions/
        valid username: admin
        valid password: Admin
        Assert '/Portal/Home' is contained in the url
        """
        time.sleep(5)
        login_ele = self.driver.find_element(By.ID, 'txtLoginid')
        login_ele.send_keys('admin')

        password_ele = self.driver.find_element(By.ID, 'txtPassword')
        password_ele.send_keys('Admin')

        login_ele_btn = self.driver.find_element(By.ID, 'btnloginText')
        login_ele_btn.click()

        time.sleep(10)

        # self.assertIn(member='Notification Center',
        #               container =self.driver.page_source,
        #               msg='Scheduling & Notification Center is visible in the page')
        WebDriverWait(self.driver, 60).until(EC.url_contains('/Portal/Home'))

    def test_failed_username(self):
        """
        http://strzw058051/SMARTSolutions/
        valid username: admin_invalid
        valid password: Admin
        Assert 'Invalid login ID or password. Please try again.'
        """
        time.sleep(5)
        login_ele = self.driver.find_element(By.ID, 'txtLoginid')
        login_ele.send_keys('admin_invalid')

        password_ele = self.driver.find_element(By.ID, 'txtPassword')
        password_ele.send_keys('Admin')

        login_ele_btn = self.driver.find_element(By.ID, 'btnloginText')
        login_ele_btn.click()

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH, '//li[contains(text(),"Invalid login ID or password. Please try again.")]')))

    def test_failed_password(self):
        """
        http://strzw058051/SMARTSolutions/
        valid username: admin
        valid password: Admin_invalid
        Assert 'Invalid login ID or password. Please try again.'

        """
        time.sleep(5)
        login_ele = self.driver.find_element(By.ID, 'txtLoginid')
        login_ele.send_keys('admin')
        password_ele = self.driver.find_element(By.ID, 'txtPassword')
        password_ele.send_keys('Admin_invalid')

        login_ele_btn = self.driver.find_element(By.ID, 'btnloginText')
        login_ele_btn.click()

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH, '//li[contains(text(),"Invalid login ID or password. Please try again.")]')))

    def test_failed_pwd_and_uname(self):
        """
        http://strzw058051/SMARTSolutions/
        valid username: admin_invalid
        valid password: Admin_invalid
        Assert 'Invalid login ID or password. Please try again.'
        """
        time.sleep(5)
        login_ele = self.driver.find_element(By.ID, 'txtLoginid')
        login_ele.send_keys('admin_invalid')

        password_ele = self.driver.find_element(By.ID, 'txtPassword')
        password_ele.send_keys('Admin_invalid')

        login_ele_btn = self.driver.find_element(By.ID, 'btnloginText')
        login_ele_btn.click()

        WebDriverWait(self.driver, 60).until(EC.visibility_of_element_located(
            (By.XPATH, '//li[contains(text(),"Invalid login ID or password. Please try again.")]')))


if __name__ == '__main__':
    pass
    # suite =unittest.TestSuite()
    # suite.addTest(MyTestCase('test_succeed'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    test_dir = './'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)
