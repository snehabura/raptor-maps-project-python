import unittest
from Demo.tests.webdriver import Driver
from Demo.pages.home import Home
from Demo.pages.jobboard import JobBoard
from Demo.values import strings
import time
from selenium.webdriver.common.action_chains import ActionChains


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.navigate(strings.base_url)
        time.sleep(2)

    def test_home_screen_components(self):
        driver = self.driver
        home = Home(driver)
        if home.validate_alert_is_present():
            home.validate_alert_is_present().click()
        time.sleep(2)

        action = ActionChains(driver)
        action.move_to_element(home.about_element()).perform()
        time.sleep(2)

        action.move_to_element(home.job_board()).click().perform()
        time.sleep(2)

    def tearDown(self):
        self.driver.instance.quit()


if __name__ == '__main__':
    unittest.main()
