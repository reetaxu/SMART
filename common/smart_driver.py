from selenium import webdriver
from tools import common_tools
from common import settings, listener, statement
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver, AbstractEventListener


class SmartDriver(webdriver.Firefox):

    @staticmethod
    def init_driver():
        common_tools.save_log('open browser: Firefox')
        return webdriver.Firefox(timeout=settings.browser_launch)

    def find_element_(self, by, value):
        common_tools.save_log(statement.para_separator)
        str_ = 'Find Element by:{0}, value:{1}'.format(by, value)
        common_tools.save_log(str_)
        return self.find_element(by, value)

    def find_elements_(self, by, value):
        common_tools.save_log(statement.para_separator)
        str_ = 'Find Elements by:{0}, value:{1}'.format(by, value)
        common_tools.save_log(str_)
        return self.find_elements(by, value)


class SmartEventFiringWebDriver(EventFiringWebDriver):

    @staticmethod
    def init_driver():
        common_tools.save_log(statement.start_to_init_browser)
        try:

            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.download.dir', 'c:\\')
            profile.set_preference('browser.download.folderList', 2)
            profile.set_preference('browser.download.manager.showWhenStarting', False)
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/pdf')

            driver_fire = webdriver.Firefox(timeout=settings.browser_launch,firefox_profile=profile)

            driver = SmartEventFiringWebDriver(driver=driver_fire,
                                               event_listener=listener.SMART_Listener())
        except:
            common_tools.save_log(statement.start_to_init_browser_fail)
        return driver

    def find_element_(self, by, value):
        common_tools.save_log(statement.para_separator)
        str_ = 'Find Element by:{0}, value:{1}'.format(by, value)
        common_tools.save_log(str_)
        return self.find_element(by, value)

    def find_elements_(self, by, value):
        common_tools.save_log(statement.para_separator)
        str_ = 'Find Elements by:{0}, value:{1}'.format(by, value)
        common_tools.save_log(str_)
        return self.find_elements(by, value)
