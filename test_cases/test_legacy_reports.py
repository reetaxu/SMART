import unittest, time, traceback
from selenium.webdriver.common.by import By
from selenium import webdriver
from common import settings, actions, smart_driver, statement, locators
from tools import common_tools
from parameterized import parameterized
from modals.report_test_result import result_report
from pages import reports


def prepare_reports_names():
    reports_ = ['DRG Change Condition Detail', 'DRG Listing by Payer',
                'Present on Admission(POA) Comparison', 'Principal Procedures',
                'Top 50 Diagnoses by Present on Admission(POA)',
                'Data Validation', 'DRG Contribution to Payer CMI', 'PEPPER Report',
                'Top 50 Diagnoses by Present on Admission(POA)',
                'Enterprise Data Validation', 'Security Administration Information by Role',
                'Inpatient Flag Information',
                'Inpatient Flag Information by Facility']

    report_names = []
    for i in common_tools.get_reports_IP_and_OP():
        report_names.append(i.report_id[0:4] + i.report_name)
    return report_names


class test_lagacy_reports(unittest.TestCase):
    driver = ''
    result_report = result_report()
    report_name = ''
    smart_pass = True
    saved_searches = ''
    numof_actual_reports_to_run = common_tools.get_reports_IP_and_OP().__len__()

    def setUp(self):
        # firfox_driver = webdriver.Firefox()
        # firfox_driver.save_screenshot()
        # driver = EventFiringWebDriver(firfox_driver, listener.SMART_Listener())
        # self.driver = webdriver.Firefox()
        self.driver = smart_driver.SmartEventFiringWebDriver.init_driver()
        # self.driver = smart_driver.SmartDriver()
        # reset msg
        self.result_report.msg = 'Success'

        # prepare saved search
        self.saved_searches = {
            'APC Reimbursement Information': 'Jon_test_PlsDoNotChange_APC',
            'Outpatient Flag Information': 'JonTest_pls_do_not_delete_it',
            'Outpatient Flag Information by Facility': 'JonTest_pls_do_not_delete_it',
            'Evaluation & Management Clinical Profile': 'Jon_test_pls_do_do_change_Evaluation',
            'DRG Listing by Payer': 'Jon_automation_test_pls_do_not_change_it',
            'Present on Admission(POA) Comparison': 'JonTestPlsDoNotChangeItPOA',
            'DRG Contribution to Payer CMI': 'JonTestPlsDoNotChangeItDRG',
            'Security Administration Information by Role': 'JonTestPlsDoNotChangeIt_SAIBR',
            'Inpatient Flag Information': 'JonTestPlsDoNotChangeIt_FlagInfor',
            'Inpatient Flag Information by Facility': 'JonTestPlsDoNotChangeIt_FlagInfor',
        }

    def tearDown(self):
        print(self.result_report.report_name)
        screenshot_path = '../auto_results/screenshots/'
        self.driver.save_screenshot(screenshot_path + self.result_report.report_name + '.png')
        # summarise result information
        self.result_report.report_module = common_tools.get_report_module(self.result_report.report_id)
        self.result_report.report_name_saved_search = self.saved_searches.get(self.report_name)
        self.result_report.screen_shot = self.result_report.report_name + ".png"
        self.result_report.steps = common_tools.get_log(self.result_report.report_name)

        # generate test reports
        common_tools.write_test_result_report_excel(self.result_report)
        common_tools.save_reports_screenshot_as_html(self.result_report)
        common_tools.write_test_result_report_word(self.result_report)

        self.driver.quit()

    # Enterprise Data Validation, Data Validation
    # @parameterized.expand(prepare_reports_names)
    def Itest_legacy_reports(self):
        report_name = 'DRG Change Condition Detail'

        reports.Reports(self.driver).find_report_double_click(report_name)
        time.sleep(10)

        # reports.Reports(self.driver).report_data_validation(report_name)

    @parameterized.expand(prepare_reports_names)
    def test_legacy_reports(self, report_name):
        report_name = 'IPSTDRG Clinical Profile'
        try:
            self.result_report.report_id = common_tools.get_report_id(report_name)
            self.result_report.report_name = report_name

            common_tools.save_log(str_='Report name: >>>>>' + report_name)

            if 'Evaluation & Management Clinical Profile' in report_name:
                report_name = 'Management Clinical Profile'

            report_name = reports.Reports(self.driver).find_report_double_click(report_name)
            self.report_name = report_name
            # wait dvCustomSearchPopup
            actions.wait_element_visibility(self.driver, By.ID, 'dvCustomSearchPopup')
            # Click View Report button
            btn_view_report_id = 'btnViewReport'
            actions.wait_element_clickable(self.driver, By.ID, btn_view_report_id)
            view_report_btn = self.driver.find_element_(By.ID, btn_view_report_id)
            view_report_btn.click()
            #
            time.sleep(1)
            no_default_filter = self.driver.find_element_(By.ID, 'dvSlidingMessageControl').value_of_css_property(
                'display')
            if no_default_filter in 'block':

                # click saved search
                if report_name in self.saved_searches.keys():
                    str_ = 'Click saved search for report - ' + report_name
                    common_tools.save_log(str_)
                    # self.result_report.report_name_saved_search = 'Jon_automation_test_pls_do_not_change_it'

                    saved_search = self.driver.find_element_(By.ID, 'showHideSearchSavedHeader')
                    saved_search_selected = self.driver.find_element_(By.XPATH,
                                                                      '//div[text()="' + self.saved_searches.get(
                                                                          report_name) + '"]')
                    saved_search_selected.click()
                # else:
                    # add one filter
                    # reports.ReportAssist.handle_no_default_filter(self.driver, report_name)

                    # click "+" icon
                    # add_icon = self.driver.find_element_(By.ID, 'btnInsertClause')
                    # add_icon.click()
                    #
                    # # add filters besides the default ones
                    # self.driver.find_element_(By.ID, 'customsearch-grid-div')
                    # self.driver.find_element_(By.XPATH,
                    #                           './/div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr')
                    # # click the last row of the CS
                    # field_last = self.driver.find_element_(By.XPATH,
                    #                                        './/div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[3]/span')
                    # field_last.click()
                    #
                    # # 遍历fileds
                    # fields_lis = self.driver.find_elements_(By.XPATH,
                    #                                         '//div[@class="k-animation-container"][last()]/div/ul/li')
                    # print(fields_lis.__len__())
                    # for li in fields_lis:
                    #     print(li.text)
                    #
                    # # click filter name
                    # field_name = 'Flag Number - Primary'
                    # field_xpath = '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + field_name + '"]'
                    # field_name_selected = self.driver.find_element_(By.XPATH, field_xpath)
                    # field_name_selected.click()
                    #
                    # # click operator
                    # operator_value = '<> Not Equal'
                    # operator = self.driver.find_element_(By.XPATH, locators.ReportLocators.operator_xpath)
                    # operator.click()
                    # operator_selected = self.driver.find_element_(By.XPATH,
                    #                                               locators.ReportLocators.operator_selected.format(
                    #                                                   operator_value))
                    # # '//div[@class="k-animation-container"][last()]/div/ul/li[text()="' + operator_value + '"]')
                    # operator_selected.click()
                    # # value
                    # value_input_xpath_ = './/div[@id="customsearch-grid"]/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[5]/div/div[6]/input'
                    # field_name_value = 'test'
                    #
                    # value_input_xpath = value_input_xpath_
                    # value_input = self.driver.find_element_(By.XPATH, value_input_xpath)
                    # value_input.click()
                    # value_input.send_keys(field_name_value)

                view_report_btn.click()
            else:
                pass

            # Go to view report window
            actions.wait_number_of_windows_to_be(self.driver, report_name)
            view_report_window = self.driver.window_handles[1]
            self.driver.switch_to.window(view_report_window)

            # 'Error Occurred'
            self.assertNotIn('Error Occurred', self.driver.page_source,
                             msg=report_name + statement.error_occurred_report_generate)
            # System.OutOfMemoryException
            if 'System.OutOfMemoryException' in self.driver.page_source:
                pass

            # export report RdlViewer_ctl01_ctl05_ctl00 RdlViewer_ctl01_ctl05_ctl00
            # RdlViewer_ctl01_ctl05_ctl00
            format_list_xpath = '//select[@id="RdlViewer_ctl01_ctl05_ctl00"]'
            # format_list = self.driver.find_element_(By.XPATH, format_list_xpath)
            format_list = self.driver.find_element(By.XPATH, format_list_xpath)
            # if report_name == 'Case Listing':
            #     format_list = self.driver.find_element_(By.ID, 'RdlViewer_ctl01_ctl05_ctl00')
            # else:
            #     format_list = self.driver.find_element_(By.ID, 'RW_ReportToolbar_ExportGr_FormatList_DropDownList')

            format_list.click()
            # select a formt
            PDF=self.driver.find_element(By.XPATH, "//option[text()='Acrobat (PDF) file']")
            PDF.click()

            expoert_btn = self.driver.find_element_(By.LINK_TEXT, 'Export')
            # expoert_btn = driver.find_element_by_id('RW_ReportToolbar_ExportGr_Export')
            expoert_btn.click()


            # assert wait_until_title_contains
            if actions.wait_document_completed(self.driver):
                self.result_report.report_test_result = reports.Reports.wait_until_title_contains(self,
                                                                                                  report_name=report_name)

            else:
                self.result_report.report_test_result = False


        except Exception as e:
            print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
            print(e.__str__())
            print(traceback.print_exc())
            str_ = '----------Listening: exception occurred----------\n' + e.__str__() + traceback.print_exc().__str__()
            common_tools.save_log(str_)
            # installing = 'We’ll be back soon!'
            self.result_report.msg = e.__str__()
            self.report_name = report_name
            print(self.report_name)
            self.result_report.report_test_result = False
            assert 'fail' in 'pass'
            print('ENDENDENDENDENDENDENDENDENDEND')


if __name__ == '__main__':
    unittest.main()
