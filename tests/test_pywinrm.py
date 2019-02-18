import unittest, winrm


class MyTestCase(unittest.TestCase):
    def test_winrm(self):
        # http://windows-host:5985/wsman
        host = 'http://169.254.16.159:5985/wsman'
        s = winrm.Session(host, auth=('Robby', '20120441012yy'))
        r = s.run_cmd('ipconfig', ['/all'])
        print('test')


if __name__ == '__main__':
    unittest.main()
