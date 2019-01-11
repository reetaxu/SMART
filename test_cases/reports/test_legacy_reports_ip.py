import unittest, time, traceback
from selenium.webdriver.common.by import By
from common import settings, actions, smart_driver
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

    reports = []

    for i in common_tools.get_reports_by(IP_or_OP='IP'):
        if 'Enterprise' in i.report_module:
            reports.append(i.report_name + '#')
        else:
            reports.append(i.report_name)

    return reports


class MyTestCase(unittest.TestCase):
    driver = ''
    result_report = result_report()
    report_name = ''
    smart_pass = True
    saved_searches = ''

    def setUp(self):
        # firfox_driver = webdriver.Firefox()
        # driver = EventFiringWebDriver(firfox_driver, listener.SMART_Listener())
        self.driver = smart_driver.SmartDriver()
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
        # take screenshot
        screenshot_path = '../../auto_results/screenshots/'
        self.driver.get_screenshot_as_file(screenshot_path + self.report_name + '.png')
        self.driver.quit()

        str_ = 'close browser'
        common_tools.save_log(str_)

        # summarise result information
        # self.result_report.report_module = common_tools.get_report_module(self.report_name)
        self.result_report.report_name = self.report_name
        self.result_report.report_name_saved_search = self.saved_searches.get(self.report_name)
        self.result_report.screen_shot = self.report_name + ".png"
        self.result_report.steps = common_tools.get_log(self.report_name)

        common_tools.write_test_result_report_word(self.result_report)
        common_tools.write_test_result_report_excel(self.result_report)
        common_tools.save_reports_screenshot_as_html(self.result_report)


    # Enterprise Data Validation, Data Validation
    # @parameterized.expand(prepare_reports_names)
    def Itest_legacy_reports(self):
        report_name = 'DRG Change Condition Detail'

        reports.Reports(self.driver).find_report_double_click(report_name)
        time.sleep(10)

        # reports.Reports(self.driver).report_data_validation(report_name)

    @parameterized.expand(prepare_reports_names)
    def test_legacy_reports(self, report_name):
        try:
            common_tools.save_log(str_= 'report_names:>>>>>'+ report_name)
            if 'Evaluation & Management Clinical Profile' in report_name:
                report_name = 'Management Clinical Profile'

            report_name = reports.Reports(self.driver).find_report_double_click(report_name)
            self.report_name = report_name

            # wait dvCustomSearchPopup
            actions.wait_element_visibility(self.driver, By.ID, 'dvCustomSearchPopup')

            # click saved search
            if report_name in self.saved_searches.keys():
                # self.result_report.report_name_saved_search = 'Jon_automation_test_pls_do_not_change_it'

                saved_search = self.driver.find_element_(By.ID, 'showHideSearchSavedHeader')
                saved_search_selected = self.driver.find_element_(By.XPATH,
                                                                  '//div[text()="' + self.saved_searches.get(
                                                                      report_name) + '"]')
                saved_search_selected.click()

            # Click View Report button
            btn_view_report_id = 'btnViewReport'
            actions.wait_element_clickable(self.driver, By.ID, btn_view_report_id)
            view_report_btn = self.driver.find_element_(By.ID, btn_view_report_id)
            view_report_btn.click()

            # Go to view report window
            actions.wait_number_of_windows_to_be(self.driver, report_name)
            view_report_window = self.driver.window_handles[1]
            self.driver.switch_to.window(view_report_window)

            # save_html_resource
            actions.wait_document_completed(self.driver)
            common_tools.save_html_resource(self.driver.page_source, report=report_name)
            # 'Error Occurred'
            self.assertNotIn('Error Occurred', self.driver.page_source,
                             msg=report_name + settings.error_report_generate)
            # System.OutOfMemoryException
            if self.driver.page_source.__contains__('System.OutOfMemoryException'):
                pass

            # assert wait_until_title_contains
            self.result_report.report_test_result = reports.Reports.wait_until_title_contains(self, report_name=report_name)
            # if report_name == 'DRG Change Condition Detail':
            #     smart_pass = actions.wait_report_title_contains(self.driver, 'DRG Change Detail')
            #     self.assertIn('DRG Change Detail', container=self.driver.title,
            #                   msg=report_name + settings.error_report_generate)
            #     assert 'DRG Change Detail' in self.driver.title
            # elif report_name == 'Top 50 Diagnoses by Present on Admission(POA)':
            #     smart_pass = actions.wait_report_title_contains(self.driver,
            #                                                     'Top 50 Other Diagnoses by Present on Admission(POA)')
            #     assert 'Top 50 Other Diagnoses' in self.driver.title
            # elif report_name == 'Management Clinical Profile':
            #     smart_pass = actions.wait_report_title_contains(self.driver, 'Evaluation')
            #     assert 'Evaluation' in self.driver.title
            # elif 'Frequency' in report_name:
            #     smart_pass = actions.wait_report_title_contains(self.driver, 'Frequency')
            #     assert 'Frequency' in self.driver.title
            # elif 'DRG Contribution to Payer CMI' in report_name:
            #     smart_pass = actions.wait_report_title_contains(self.driver, 'DRG Contribution to CMI by Payer')
            #     assert 'DRG Contribution to CMI by Payer' in self.driver.title
            # elif report_name in report_name:
            #     smart_pass = actions.wait_report_title_contains(self.driver, report_name)
            #     assert report_name in self.driver.title
            # else:
            #     smart_pass = False

            # if not smart_pass:
            #     self.result_report.report_test_result = 'Fail'
            # else:
            #     self.result_report.report_test_result = 'Pass'

        except Exception as e:
            print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
            print(e.__str__())
            print(traceback.print_exc())
            str_= 'EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\n'+ e.__str__() + traceback.print_exc().__str__()
            common_tools.save_log(str_)
            # installing = 'We’ll be back soon!'
            self.result_report.msg = e.__str__()
            self.report_name = report_name.rstrip('#')
            self.result_report.report_test_result = 'Fail'
            assert 'fail' in 'pass'




if __name__ == '__main__':
    unittest.main()
