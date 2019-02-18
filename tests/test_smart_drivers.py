import unittest
from common import smart_driver, settings, actions
from selenium.webdriver.common.by import By


class MyTestCase(unittest.TestCase):
    def Itest_SmartDriver(self):
        driver = smart_driver.SmartDriver.init_driver()
        driver.get('https://selenium-python.readthedocs.io/api.html')
        # print(driver.get_log(log_type='browser'))

    def test_SmartEventFiringWebDriver(self):
        driver = smart_driver.SmartEventFiringWebDriver.init_driver()
        driver.get(settings.url)

        login_ele = driver.find_element_(By.ID, 'txtLoginid')
        login_ele.send_keys('admin')

        password_ele = driver.find_element_(By.ID, 'txtPassword')
        password_ele.send_keys('Admin')

        login_ele_btn = driver.find_element_(By.ID, 'btnloginText')
        login_ele_btn.click()
        driver.execute_script('$("#btnloginText").click()')
        # driver.execute_script('$("#btnloginText").dblclick()')

        # click Inpatient
        actions.wait_element_clickable(driver, By.ID, 'aSlideMenuSelModuleSIP101')
        actions.wait_element_invisibility(driver, By.CLASS_NAME, 'modalOverlay')
        inpatient = driver.find_element_(By.ID, 'aSlideMenuSelModuleSIP101')
        inpatient.click()

        # Click "report"
        report = driver.find_element_(By.ID, 'aIPModuleWorkplans')
        report.click()

        # click enterprise_reports_link
        standard_reports_link_xpath = '//span[text()="Inpatient Standard Reports"]'
        enterprise_reports_link = '//span[text()="Inpatient Enterprise Reports"]'

        actions.wait_element_clickable(driver, By.XPATH, standard_reports_link_xpath)
        reports_link = driver.find_element_by_xpath(standard_reports_link_xpath)
        reports_link.click()

        # enter report name
        report_name_input_id = 'txtSearch'
        report_name_input = driver.find_element_(By.ID, report_name_input_id)
        actions.wait_element_clickable(driver, By.ID, report_name_input_id)
        report_name_input.clear()
        report_name_input.send_keys('Coder Information')

        # click search button
        report_search_btn_id = 'spnSearch'
        report_search_btn = driver.find_element_(By.ID, report_search_btn_id)
        actions.wait_element_clickable(driver, By.ID, report_search_btn_id)
        report_search_btn.click()

        # find and Open report
        actions.wait_element_clickable(driver, By.PARTIAL_LINK_TEXT, 'Coder Information')
        report_enter_link = driver.find_element_by_partial_link_text('Coder Information')

        # script = '$("a:contains(Coder Information)").dblclick()'
        script = '$("a:contains(Coder Information)").click()'
        driver.execute_script(script)
        script = "var evt = document.createEvent('MouseEvents');" \
                 + "evt.initMouseEvent('dblclick',true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0,null);" \
                 + "arguments[0].dispatchEvent(evt);"
        # ActionChains(self.driver).move_to_element(report_enter_link).double_click()
        # time.sleep(2)
        driver.execute_script(script, report_enter_link)


if __name__ == '__main__':
    unittest.main()
