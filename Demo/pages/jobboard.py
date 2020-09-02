from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

class JobBoard:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15
        self.jobBoard = WebDriverWait(self.driver.instance, self.timeout).until(
            EC.visibility_of_element_located((
                By.ID, "menu-item-5094")))
        self.qa = WebDriverWait(self.driver.instance, self.timeout).until(
            EC.visibility_of_element_located((
                By.XPATH, "m//*[@id=\"et-boc\"]/div/div[2]/div/div[1]/div[9]/div/h4/b")))

    def click_job_board(self):
        try:
            action = ActionChains(self.driver)
            assert action.move_to_element(self.jobBoard).click().perform()
        except TimeoutException as ex:
            print("Element unclickable after {0} seconds".format(self.timeout))

    def qa(self):
        try:
            assert self.qa
        except TimeoutException as ex:
            print("Element unclickable after {0} seconds".format(self.timeout))
