import time
from selenium import webdriver;
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.Firefox()
driver.maximize_window()
driver.get("https://raptormaps.com/")
time.sleep(2)

alert: WebElement = driver.find_element_by_id("hs-eu-decline-button")
if alert.is_displayed():
    alert.click()
time.sleep(2)

aboutElement: WebElement = driver.find_element_by_id("menu-item-5086")
action = ActionChains(driver)
action.move_to_element(aboutElement).perform()
time.sleep(2)

jobBoard: WebElement = driver.find_element_by_id("menu-item-5094")
action.move_to_element(jobBoard).click().perform()
time.sleep(2)

qa: WebElement = driver.find_element_by_xpath("//*[@id=\"et-boc\"]/div/div[2]/div/div[1]/div[9]/div/h4/b")
driver.execute_script("arguments[0].scrollIntoView();", qa)

jD = "Raptor Maps software is used by a global customer base in the clean energy sector. Quality Assurance is a critical aspect of our fast-paced development cycle. We have a full-time quality assurance position available in our software engineering team.";

if qa.is_displayed():
    print("QA Job found")
    assert jD in driver.find_element_by_xpath("//*[@id=\"et-boc\"]/div/div[2]/div/div[1]/div[9]/div/p[2]/span").text
    # Assert.assertEquals(jD, driver.find_element_by_xpath("//*[@id=\"et-boc\"]/div/div[2]/div/div[1]/div[9]/div/p[2]/span").text)
else:
    print("QA Job not found")

if "Astronaut" in driver.page_source:
    print("AstronautJob found ::::")
else:
    print("AstronautJob not found::::")

assert "No results found." not in driver.page_source
driver.close()
