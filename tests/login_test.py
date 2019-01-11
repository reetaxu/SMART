import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from common import settings, actions, listener
from selenium.webdriver.common.action_chains import ActionChains
from tools import common_tools
from parameterized import parameterized
from modals.report_test_result import result_report


def prepare_reports_names():
    reports = []
    for i in common_tools.get_reports_by(IP_or_OP='IP'):
        reports.append(i.report_name)

    return reports


class MyTestCase(unittest.TestCase):
    driver = ''
    result_report = result_report()
    report_name = ''

    def setUp(self):

        firfox_driver = webdriver.Firefox()
        # driver = EventFiringWebDriver(firfox_driver, listener.SMART_Listener())
        self.driver = firfox_driver

    def tearDown(self):

        self.result_report.report_module = 'IP Standard'
        self.result_report.report_name = self.report_name
        self.result_report.report_name_saved_search = 'None'
        self.result_report.screen_shot = self.report_name + "png"

        self.driver.get_screenshot_as_file(self.report_name + '.png')
        common_tools.write_test_result_report_word(self.result_report)
        common_tools.write_test_result_report_excel(self.result_report)

        self.driver.quit()

    @parameterized.expand(prepare_reports_names)
    def test_legacy_reports(self, report_name):

        self.report_name = report_name

        self.driver.get(settings.url)

        login_ele = self.driver.find_element_by_id('txtLoginid')
        password_ele = self.driver.find_element_by_id('txtPassword')
        login_ele_btn = self.driver.find_element_by_id('btnloginText')

        login_ele.clear()
        login_ele.send_keys('admin')

        password_ele.clear()
        password_ele.send_keys('Admin')
        login_ele_btn.click()

        # print(driver.page_source)
        print('----------------' + self.driver.title)

        actions.wait_element_clickable(self.driver, By.ID, 'aSlideMenuSelModuleSIP101')
        actions.wait_element_invisibility(self.driver, By.CLASS_NAME, 'modalOverlay')
        self.driver.find_element_by_id('aSlideMenuSelModuleSIP101').click()

        # Click "report"
        report = self.driver.find_element_by_id('aIPModuleWorkplans')
        report.click()

        # click enterprise_reports_link
        enterprise_reports_link_xpath = '//span[text()="Inpatient Standard Reports"]'
        actions.wait_element_clickable(self.driver, By.XPATH, enterprise_reports_link_xpath)
        enterprise_reports_link = self.driver.find_element_by_xpath(enterprise_reports_link_xpath)
        enterprise_reports_link.click()

        # enter report name
        report_name_input_id = 'txtSearch'
        report_name_input = self.driver.find_element_by_id(report_name_input_id)
        actions.wait_element_clickable(self.driver, By.ID, report_name_input_id)
        report_name_input.clear()
        report_name_input.send_keys(report_name)

        # click search button
        report_search_btn_id = 'spnSearch'
        report_search_btn = self.driver.find_element_by_id(report_search_btn_id)
        actions.wait_element_clickable(self.driver, By.ID, report_search_btn_id)
        report_search_btn.click()

        # find and Open report
        actions.wait_element_clickable(self.driver, By.PARTIAL_LINK_TEXT, report_name)
        report_enter_link = self.driver.find_element_by_partial_link_text(report_name)
        ActionChains(self.driver).double_click(report_enter_link).perform()

        # wait dvCustomSearchPopup
        actions.wait_element_visibility(self.driver, By.ID, 'dvCustomSearchPopup')

        # Click View Report button
        btn_view_report_id = 'btnViewReport'
        # actions.wait_element_visibility(driver, By.ID, report_search_btn_id)
        # actions.wait_element_presence(driver, By.ID, report_search_btn_id)
        actions.wait_element_clickable(self.driver, By.ID, report_search_btn_id)
        view_report_btn = self.driver.find_element_by_id(btn_view_report_id)
        view_report_btn.click()

        # Go to view report window
        actions.wait_number_of_windows_to_be(self.driver, report_name)
        view_report_window = self.driver.window_handles[1]
        self.driver.switch_to.window(view_report_window)

        # assertion
        actions.wait_document_completed(self.driver)
        # 'Error Occurred'
        self.assertNotIn('Error Occurred', self.driver.page_source, msg=report_name + settings.error_report_generate)
        # report name in the report
        self.assertIn('Data Comparison - DRG CC/MCCs', self.driver.page_source,
                      msg=report_name + settings.error_report_generate)
        # out of memory
        if self.driver.page_source.__contains__('System.OutOfMemoryException'):
            pass

        # assert wait_until_title_contains
        if report_name == 'DRG Change Condition Detail':
            smart_pass = actions.wait_until_title_contains(self.driver, 'DRG Change Detail')
            self.assertIn('DRG Change Detail', container=self.driver.title,
                          msg=report_name + settings.error_report_generate)
            assert 'DRG Change Detail' in self.driver.title
        elif report_name == 'Top 50 Diagnoses by Present on Admission(POA)':
            smart_pass = actions.wait_report_title_contains(self.driver,
                                                            'Top 50 Other Diagnoses by Present on Admission(POA)')
            assert 'Top 50 Other Diagnoses' in self.driver.title
        elif report_name == 'Management Clinical Profile':
            smart_pass = actions.wait_report_title_contains(self.driver, 'Evaluation')
            assert 'Evaluation' in self.driver.title
        elif 'Frequency' in report_name:
            smart_pass = actions.wait_report_title_contains(self.driver, 'Frequency')
            assert 'Frequency' in self.driver.title
        elif 'DRG Contribution to Payer CMI' in report_name:
            smart_pass = actions.wait_report_title_contains(self.driver, 'DRG Contribution to CMI by Payer')
            assert 'DRG Contribution to CMI by Payer' in self.driver.title
        elif report_name in report_name:
            smart_pass = actions.wait_report_title_contains(self.driver, report_name)
            assert report_name in self.driver.title
        else:
            smart_pass = False

        result_report.report_test_result = 'Pass'


if __name__ == '__main__':
    unittest.main()
