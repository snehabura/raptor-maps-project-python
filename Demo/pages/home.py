from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


class Home:

    def __init__(self, driver):

        self.driver = driver
        self.timeout = 15

        self.alert = WebDriverWait(self.driver.instance, self.timeout).until(
            EC.visibility_of_element_located((
                By.ID, "hs-eu-decline-button")))

        self.aboutElement = WebDriverWait(self.driver.instance, self.timeout).until(
            EC.visibility_of_element_located((
                By.ID, "menu-item-5086")))

        self.jobBoard = WebDriverWait(self.driver.instance, self.timeout).until(
            EC.visibility_of_element_located((
                By.ID, "menu-item-5094")))

        self.qa = WebDriverWait(self.driver.instance, self.timeout).until(
            EC.visibility_of_element_located((
                By.XPATH, "m//*[@id=\"et-boc\"]/div/div[2]/div/div[1]/div[9]/div/h4/b")))

    def validate_alert_is_present(self):
        try:
            assert self.alert.is_displayed()
        except TimeoutException as ex:
            print ("Element unclickable after {0} seconds".format(self.timeout))

    def about_element(self):
        try:
            assert self.aboutElement
        except TimeoutException as ex:
            print ("Element unclickable after {0} seconds".format(self.timeout))

    def job_board(self):
        try:
            assert self.jobBoard
        except TimeoutException as ex:
            print ("Element unclickable after {0} seconds".format(self.timeout))

    def qa(self):
        try:
            assert self.qa
        except TimeoutException as ex:
            print ("Element unclickable after {0} seconds".format(self.timeout))