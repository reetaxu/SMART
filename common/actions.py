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
            str_ = 'Wait until report view window is open: ' + report + '=pass'
            common_tools.save_log(str_)
        except Exception as e:
            str_ = 'Wait until report view window is open: ' + report + '=Fail: ' + e.__str__()
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
            str_ = 'Wait until report window title is: ' + report + '= Pass'
            common_tools.save_log(str_)
        except Exception as e:
            str_ = 'Wait until report window title is: ' + report + '= Fail: ' + e.__str__()
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
    str_ = 'Wait until element is visible, by: {0}, by_target: {1}'.format(by, by_target)
    common_tools.save_log(str_)
    try:
        WebDriverWait(driver, settings.timeout).until(
            EC.visibility_of_element_located((by, by_target)))

        str_ = 'Element is visible, by: {0}, value: {1}'.format(by, by_target)
        common_tools.save_log(str_)

    except Exception as e:
        str_ = 'Element is not visible, by: {0}, value: {1}'.format(by, by_target)
        common_tools.save_log(str_)
        common_tools.save_log(e.__str__())


def wait_element_invisibility(driver, by, by_target):
    str_ = 'Wait until element is invisible, by: {0}, by_target: {1}'.format(by, by_target)
    common_tools.save_log(str_)
    WebDriverWait(driver, settings.timeout).until(
        EC.invisibility_of_element_located((by, by_target)))


def wait_element_clickable(driver, by, by_target):
    str_ = 'Wait until element is clickable, by: {0}, value: {1}'.format(by, by_target)
    common_tools.save_log(str_)
    try:
        element = WebDriverWait(driver, settings.timeout).until(
            EC.element_to_be_clickable((by, by_target))
        )
    except Exception as e:
        str_ = 'Wait until element is clickable: exception occurred, by: {0}, value: {1}'.format(by, by_target)
        common_tools.save_log(str_)
        common_tools.save_log(e.__str__())


def wait_document_completed(driver):
    smart_pass = True

    for i in range(1, settings.login_timeout):
        status = driver.execute_script('return document.readyState')
        str_ = 'Wait until paged loaded fully---wait: ' + i.__str__() + 's ' + status
        common_tools.save_log(str_)

        if ('complete' == status):
            smart_pass = True
            break
        else:
            smart_pass = False
            time.sleep(1)

    if not smart_pass:
        str_ = 'Wait until paged loaded fully, page takes too long to load, report name: {0}, seconds: {1}'.format(
            driver.title, settings.login_timeout)
        common_tools.save_log(str_)
    else:
        pass

    return smart_pass
