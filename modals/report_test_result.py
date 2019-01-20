class result_report(object):

    def __init__(self, report_id='Default Empty', report_module='IP Standard',
                 report_name='Default Empty', report_name_saved_search='',
                 report_test_result='Fail', screen_shot='', msg='Success', steps='Default Empty'):
        self.report_id = report_id
        self.report_module = report_module
        self.report_name = report_name
        self.report_name_saved_search = report_name_saved_search
        self.report_test_result = report_test_result
        self.screen_shot = screen_shot
        self.msg = msg
        self.steps = steps
