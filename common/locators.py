from selenium.webdriver.common.by import By


# for maintainability we can seperate web objects by page name

class Common(object):
    modal_overlay = (By.CLASS_NAME, 'modalOverlay')


class LoginPageLocators(object):
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT = (By.ID, 'signInSubmit-input')
    ERROR_MESSAGE = (By.ID, 'message_error')
