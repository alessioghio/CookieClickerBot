from selenium import webdriver
from selenium.webdriver.common import keys
import time

class cookieBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.flag = 1
        self.hire = 1

    def closeBrowser(self):
        self.driver.close()

    def openCookieClicker(self):
        driver = self.driver
        driver.get("http://orteil.dashnet.org/cookieclicker/")
        time.sleep(4)
        button = driver.find_element_by_xpath("//a[@href='#null']")
        button.click()
        time.sleep(1)

    def clickCookie(self):
        driver = self.driver
        cookie = driver.find_element_by_id("bigCookie")
        cookie.click()

    def hireGrandma(self):
        driver = self.driver
        try:
            grandma = driver.find_element_by_xpath("//div[@id='product1'][@class='product unlocked enabled']")
            grandma.click()
            try:
                grandmaNum = driver.find_element_by_xpath("//div[@id='productOwned1']").text
                grandmaNum = int(grandmaNum)
                if grandmaNum%10 == 0:
                    self.hire = 0
            except:
                pass
        except:
            pass

    def closeAchievement(self):
        driver = self.driver
        try:
            close = driver.find_element_by_xpath("//div[@class='close']")
            close.click()
        except:
            pass

    def buyUpgrade(self):
        driver = self.driver
        try:
            upgrade = driver.find_element_by_xpath("//div[@class='crate upgrade enabled']")
            upgrade.click()
            self.hire = 1
        except:
            pass


grandmaArmy = cookieBot()
grandmaArmy.openCookieClicker()

while(grandmaArmy.flag):
    grandmaArmy.clickCookie()
    if grandmaArmy.hire == 1:
        grandmaArmy.hireGrandma()
    else:
        grandmaArmy.buyUpgrade()
    grandmaArmy.closeAchievement()
