import unittest, openpyxl
from modals.report_test_result import result_report
from tools import common_tools


class MyTestCase(unittest.TestCase):

    def Utest_get_report_module(self):
        m = common_tools.get_report_module('Case Listing')
        print(m)

    def test_get_log(self):
        logs = common_tools.get_log('Case Listing')
        print(logs)


    def Itest_get_logs(self):

        logs = common_tools.get_logs()
        print(logs.__len__())
        for i in logs:
            print(i)

    def Atest_save_log(self):
        str_ = 'report name'
        common_tools.save_log(str_)

    def Ttest_save_reports_screenshot_as_html(self):
        result = result_report(report_module='ttte',
                               report_name='ere',
                               report_test_result='Fail',
                               screen_shot='Coder Information.png'
                               )
        common_tools.save_reports_screenshot_as_html(result)

    def Ttest_save_html_resource(self):
        common_tools.save_html_resource('etset', 'report')

    def Atest_get_reports_by(self):
        reports = common_tools.get_reports_by(IP_or_OP='IP')
        for i in reports:
            print(i.report_module)

    def Ttest_write_test_result_report(self):
        test_result_report = result_report(report_name='test11', report_module='standard',
                                           report_name_saved_search='saved search',
                                           report_test_result='Fail',
                                           screen_shot='Data Comparison.png'
                                           )
        f = '../auto_results/test_results/legacy reports auto test result.xlsx'
        path_screenshot = r'C:\Users\yyang212\PycharmProjects\SMART_Auto\auto_results\screenshots\\' + test_result_report.screen_shot
        wb = openpyxl.load_workbook(f)
        ip_sheet = wb['IP']

        ip_sheet.append([
            test_result_report.report_module,
            test_result_report.report_name,
            test_result_report.report_name_saved_search,
            test_result_report.report_test_result,
        ])

        row_max = ip_sheet.max_row

        # Result set condional format

        # redFill = PatternFill(start_color='FFEE1111', end_color='FFEE1111', fill_type='solid')
        # greenFill = PatternFill(start_color='3CB371', end_color='3CB371', fill_type='solid')

        # ip_sheet.conditional_formatting.add('D2:D1000',
        #                               FormulaRule(formula=['NOT(ISERROR(SEARCH("Pass",E4)))'], stopIfTrue=True,
        #                                           fill=greenFill))
        # ip_sheet.conditional_formatting.add('D2:D1000',
        #                               FormulaRule(formula=['NOT(ISERROR(SEARCH("Fail",E4)))'], stopIfTrue=True,
        #                                           fill=redFill))
        #
        # ip_sheet.conditional_formatting.add('D2:D1000', FormulaRule(formula=['Fail'], stopIfTrue=True, fill=redFill))

        # ip_sheet.conditional_formatting.add('D2:D1000',
        #                                  CellIsRule(operator='=', formula=['"Pass"'], stopIfTrue=True, fill=greenFill))
        # ip_sheet.conditional_formatting.add('D2:D1000',
        #                                     CellIsRule(operator='=', formula=['"Fail"'], stopIfTrue=True, fill=redFill))

        # screenshot 设置超链接
        ip_sheet.cell(row=row_max, column=5).hyperlink = path_screenshot
        ip_sheet.cell(row=row_max, column=5).style = 'Hyperlink'
        ip_sheet.cell(row=row_max, column=5).value = test_result_report.screen_shot

        wb.save('../auto_results/test_results/legacy reports auto test result.xlsx')


if __name__ == '__main__':
    unittest.main()
