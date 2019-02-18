from selenium import webdriver
from selenium.webdriver.support.events import EventFiringWebDriver
from selenium.webdriver.support.events import AbstractEventListener
import unittest, time

class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        driver.get_screenshot_as_file("C:/Error.png")

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()  # Set Firefox browser
        self.driver3 = EventFiringWebDriver(self.driver, ScreenshotListener())
        self.driver.maximize_window()  # Maximize window
        time.sleep(0.30)  # Wait 30 seconds



if __name__ == '__main__':
    unittest.main()
