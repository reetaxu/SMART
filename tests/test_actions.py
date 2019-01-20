import unittest,os


class MyTestCase(unittest.TestCase):
    def test_something(self):
        file_path = '../auto_results/report_view_html_resources/report.html'
        page_resourece = 'test'
        f= open(file_path,'w')
        f.write(page_resourece)
        f.close()



if __name__ == '__main__':
    unittest.main()
