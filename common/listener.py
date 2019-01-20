from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener
from selenium.webdriver.common.by import By
from tools import common_tools
from common import actions, statement


class SMART_Listener(AbstractEventListener):

    def before_navigate_to(self, url, driver):
        str_ = 'Navigating to url: ' + url
        common_tools.save_log(str_)

    def after_navigate_to(self, url, driver):
        str_ = 'Navigated to url: ' + url
        common_tools.save_log(str_)

    def before_execute_script(self, script, driver):
        if 'initMouseEvent' in script:
            str_ = 'Going to click report name'
            common_tools.save_log(str_)

    def after_execute_script(self, script, driver):
        if 'initMouseEvent' in script:
            str_ = 'Report name is clicked'
            common_tools.save_log(str_)
            common_tools.save_log(statement.para_separator)

    def before_change_value_of(self, element, driver):
        pass

    def after_change_value_of(self, element, driver):
        str_ = 'Values entered'
        common_tools.save_log(str_)

    def before_find(self, by, value, driver):
        if 'modalOverlay' not in value:
            actions.wait_element_clickable(driver=driver, by=by, by_target=value)
            actions.wait_element_visibility(driver=driver, by=by, by_target=value)

    def after_find(self, by, value, driver):
        str_ = 'Element found: by-{0}, value-{1}'.format(by, value)
        if 'modalOverlay' not in value:
            actions.wait_element_clickable(driver=driver, by=by, by_target=value)
        common_tools.save_log(str_)
        pass

    def before_click(self, element, driver):
        pass

    def after_click(self, element, driver):
        str_ = 'Element Clicked'
        common_tools.save_log(str_)
        common_tools.save_log(statement.para_separator)

    def after_close(self, driver):
        str_ = 'close page: {0}'.format(driver.title)
        common_tools.save_log(str_)

    def after_quit(self, driver):
        str_ = 'close browser: {0}'.format(driver.title)
        common_tools.save_log(str_)

    def on_exception(self, exception, driver):
        str_ = '----------Listening: exception occurred----------'
        common_tools.save_log(str_)
        common_tools.save_log(exception.__str__())
