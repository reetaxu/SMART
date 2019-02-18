from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class Common(object):
    modal_overlay = (By.CLASS_NAME, 'modalOverlay')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT = (By.ID, 'signInSubmit-input')
    ERROR_MESSAGE = (By.ID, 'message_error')


class ReportLocators(object):
    operator_xpath = '//div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[4]/span'
    operator_selected = (By.XPATH, '//div[@class="k-animation-container"][last()]/div/ul/li[text()={0}]')
    # operator_selected = (By.XPATH, '//div[@class="k-animation-container"][last()]/div/ul/li[text()={0}]')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT = (By.ID, 'signInSubmit-input')
    ERROR_MESSAGE = (By.ID, 'message_error')


class CustomSearch(object):
    operator_xpath = '//div[@id="customsearch-grid-div"]/div/div[@class="k-grid-content"]/table/tbody/tr[last()]/td[4]/span'
    operator_selected = (By.XPATH, '//div[@class="k-animation-container"][last()]/div/ul/li[text()={0}]')
    # operator_selected = (By.XPATH, '//div[@class="k-animation-container"][last()]/div/ul/li[text()={0}]')
