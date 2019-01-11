from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener


class SMART_Listener(AbstractEventListener):

    # def before_navigate_to(self, url, driver):
    #     print('-------------SMART_Listener-----------')
    #     print('navigating_to_url:' + url)
    #
    # def after_navigate_to(self, url, driver):
    #     print('after_navigate_to:' + url)
    #     pass
    #
    # def before_navigate_back(self, driver):
    #     pass
    #
    # def after_navigate_back(self, driver):
    #     pass
    #
    # def before_navigate_forward(self, driver):
    #     pass
    #
    # def after_navigate_forward(self, driver):
    #     pass
    #
    # def before_find(self, by, value, driver):
    #     print('before_find {0}-{1}'.format(by,value))
    #     pass
    #
    # def after_find(self, by, value, driver):
    #     print('after_find {0}-{1}'.format(by, value))
    #     pass
    #
    # def before_click(self, element, driver):
    #     print('before_click {0}'.format(element))
    #     pass
    #
    # def after_click(self, element, driver):
    #     print('after_click {0}'.format(element))
    #     pass
    #
    # def before_change_value_of(self, element, driver):
    #     print('before_change_value_of {0}'.format(element))
    #     pass
    #
    # def after_change_value_of(self, element, driver):
    #     print('after_change_value_of {0}'.format(element))
    #     pass
    #
    # def before_execute_script(self, script, driver):
    #     print('before_execute_script {0}'.format(script))
    #     pass
    #
    # def after_execute_script(self, script, driver):
    #     print('after_execute_script {0}'.format(script))
    #     pass
    #
    # def before_close(self, driver):
    #     print('before_close {0}'.format(driver.title))
    #     pass
    #
    # def after_close(self, driver):
    #     print('after_close {0}'.format(driver.title))
    #     pass

    # def before_quit(self, driver):
    #     pass
    #
    # def after_quit(self, driver):
    #     pass

    def on_exception(self, exception, driver):
        # update excel file
        print('EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE')
        print(type(exception))
        print(exception)
        pass
