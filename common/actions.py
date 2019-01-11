from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from common import settings, actions, listener
from tools import common_tools

import time


def error_occurred_handle(driver, report):
    smart_pass = True
    return smart_pass


def wait_number_of_windows_to_be(driver, report):
    smart_pass = error_occurred_handle(driver, report)
    if smart_pass:
        try:
            element = WebDriverWait(driver, settings.timeout).until(EC.number_of_windows_to_be(2))
            str_ = 'wait_number_of_windows_to_be=2' + element.__str__() + '=pass'
            common_tools.save_log(str_)
        except Exception as e:
            str_ = 'wait_number_of_windows_to_be=2' + report + '=Fail: ' + e.__str__()
            common_tools.save_log(str_)
            smart_pass = False
    else:
        pass
    return smart_pass


def wait_report_title_contains(driver, report):
    smart_pass = error_occurred_handle(driver, report)
    if smart_pass:
        try:
            WebDriverWait(driver, settings.report_generate_timeout).until(EC.title_contains(report))
            str_ = 'wait_report_title_contains=' + report + '=Pass'
            common_tools.save_log(str_)
        except Exception as e:
            str_ = 'wait_report_title_contains-' + report + '=Fail: ' + e.__str__()
            common_tools.save_log(str_)
            smart_pass = False
    else:
        pass
    return smart_pass


def wait_element_presence(driver, by, by_target):
    str_ = 'wait_element_presence by: {0}, by_target: {1}'.format(by, by_target)
    common_tools.save_log(str_)
    element = WebDriverWait(driver, settings.timeout).until(
        EC.presence_of_element_located((by, by_target))
    )


def wait_element_visibility(driver, by, by_target):
    str_ = 'wait_element_visibility by: {0}, by_target: {1}'.format(by, by_target)
    common_tools.save_log(str_)
    element = WebDriverWait(driver, settings.timeout).until(
        EC.visibility_of_element_located((by, by_target)))


def wait_element_invisibility(driver, by, by_target):
    str_ = 'wait_element_invisibility by: {0}, by_target: {1}'.format(by, by_target)
    common_tools.save_log(str_)
    wait_document_completed(driver)
    WebDriverWait(driver, settings.timeout).until(
        EC.invisibility_of_element_located((by, by_target)))


def wait_element_clickable(driver, by, by_target):
    str_ = 'wait_element_clickable-by: {0}, by_target: {1}'.format(by, by_target)
    common_tools.save_log(str_)
    element = WebDriverWait(driver, settings.timeout).until(
        EC.element_to_be_clickable((by, by_target))
    )


def wait_document_completed(driver):
    responsed = False

    for i in range(1, settings.login_timeout):
        status = driver.execute_script('return document.readyState')
        str_ = 'wait_document_completed---wait: ' + i.__str__() + 's ' + status
        common_tools.save_log(str_)

        if ('complete' == status):
            responsed = True
            break
        else:
            time.sleep(1)

    if not responsed:
        str_ = 'wait_document_completed, page takes too long to response: ' + driver.title
        common_tools.save_log(str_)
    else:
        pass

    return responsed
