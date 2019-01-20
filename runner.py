import unittest

if __name__ == '__main__':
    # Runner 1
    # XML control test cases
    # suite =unittest.TestSuite()
    # suite.addTest(MyTestCase('test_succeed'))
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    # Runner 2
    test_dir = './test_cases/'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    runner = unittest.TextTestRunner()
    runner.run(discover)
