import unittest
from modals.report_test_result import result_report
from tools import common_tools
import sys_tools


class MyTestCase(unittest.TestCase):

    def test_system_tool(self):
        print(sys_tools.base_path)

    def Itest_get_report_id(self):
        print(common_tools.get_report_id('IPENSMART Reimbursement Activity'))

    def Itest_get_report_module(self):
        m = common_tools.get_report_module('OPSTReport092')
        print(m)
        m = common_tools.get_report_module('OPENReport120')
        print(m)
        m = common_tools.get_report_module('IPENReport086')
        print(m)

    def Itest_get_log(self):

        print(common_tools.get_log('DRG Contribution to CMI'))


    def Itest_get_logs(self):

        logs = common_tools.get_logs()
        print(logs.__len__())
        for i in logs:
            print(i)

    def Itest_save_log(self):
        str_ = 'report name'
        common_tools.save_log(str_)

    def Itest_save_reports_screenshot_as_html(self):
        result = result_report(report_module='ttte',
                               report_name='ere',
                               report_test_result='Fail',
                               screen_shot='Diagnosis Code Usage by Payer.png'
                               )
        common_tools.save_reports_screenshot_as_html(result)

    def Ttest_save_html_resource(self):
        common_tools.save_html_resource('etset', 'report')

    def Itest_get_reports_IP_and_OP(self):
        report_names = []

        for i in common_tools.get_reports_IP_and_OP():
            report_names.append(i.report_id[0:4] + i.report_name)

        for i in report_names:
            print(i)



    def Itest_write_test_result_report_excel(self):
        test_result_report = result_report(report_name='test11', report_module='standard',
                                           report_name_saved_search='saved search',
                                           report_test_result='Fail',
                                           screen_shot='Coder Information.png'
                                           )
        common_tools.write_test_result_report_excel(test_result_report)
        common_tools.write_test_result_report_word(test_result_report)


if __name__ == '__main__':
    unittest.main()
