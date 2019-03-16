from selenium import webdriver
from selenium.webdriver.common import keys
import time
import math
import threading

objectives = [100, 1100, 12000, 130000, 1.4*math.pow(10,6), 20*math.pow(10,6),
             330*math.pow(10,6), 5.1*math.pow(10,9), 75*math.pow(10,9),
             1*math.pow(10,12), 141*math.pow(10,12), 1701*math.pow(10,12),
             2.11*math.pow(10,15), 26*math.pow(10,15), 310*math.pow(10,15)]

class cookieBot:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.flag = 0
        self.cookiesNum = 0
        self.buyFlag = 0
        self.startTime = 0
        self.endTime = 0

    def closeBrowser(self):
        self.driver.close()
        self.driver.quit()

    def openCookieClicker(self):
        driver = self.driver
        driver.get("http://orteil.dashnet.org/cookieclicker/")
        time.sleep(4)
        try:
            button = driver.find_element_by_xpath("//a[@href='#null']")
            button.click()
        except:
            pass
        time.sleep(1)

    def loadFile(self):
        driver = self.driver
        try:
            options = driver.find_element_by_id("prefsButton")
            options.click()
            try:
                time.sleep(1)
                driver.find_element_by_id("FileLoadInput").send_keys("address of txt file")
                time.sleep(1)
                closeMenu = driver.find_element_by_xpath("//div[@class='close menuClose']")
                closeMenu.click()
                time.sleep(2)

                try:
                    driver.find_element_by_xpath("//div[@id='row15'][@class='row enabled']")
                    self.flag = 15
                except:
                    try:
                        driver.find_element_by_xpath("//div[@id='row14'][@class='row enabled']")
                        self.flag = 14
                    except:
                        try:
                            driver.find_element_by_xpath("//div[@id='row13'][@class='row enabled']")
                            self.flag = 13
                        except:
                            try:
                                driver.find_element_by_xpath("//div[@id='row12'][@class='row enabled']")
                                self.flag = 12
                            except:
                                try:
                                    driver.find_element_by_xpath("//div[@id='row11'][@class='row enabled']")
                                    self.flag = 11
                                except:
                                    try:
                                        driver.find_element_by_xpath("//div[@id='row10'][@class='row enabled']")
                                        self.flag = 10
                                    except:
                                        try:
                                            driver.find_element_by_xpath("//div[@id='row9'][@class='row enabled']")
                                            self.flag = 9
                                        except:
                                            try:
                                                driver.find_element_by_xpath("//div[@id='row8'][@class='row enabled']")
                                                self.flag = 8
                                            except:
                                                try:
                                                    driver.find_element_by_xpath("//div[@id='row7'][@class='row enabled']")
                                                    self.flag = 7
                                                except:
                                                    try:
                                                        driver.find_element_by_xpath("//div[@id='row6'][@class='row enabled']")
                                                        self.flag = 6
                                                    except:
                                                        try:
                                                            driver.find_element_by_xpath("//div[@id='row5'][@class='row enabled']")
                                                            self.flag = 5
                                                        except:
                                                            try:
                                                                driver.find_element_by_xpath("//div[@id='row4'][@class='row enabled']")
                                                                self.flag = 4
                                                            except:
                                                                try:
                                                                    driver.find_element_by_xpath("//div[@id='row3'][@class='row enabled']")
                                                                    self.flag = 3
                                                                except:
                                                                    try:
                                                                        driver.find_element_by_xpath("//div[@id='row2'][@class='row enabled']")
                                                                        self.flag = 2
                                                                    except:
                                                                        try:
                                                                            driver.find_element_by_xpath("//div[@id='row1'][@class='row enabled']")
                                                                            self.flag = 1
                                                                        except:
                                                                            pass

            except:
                print("Could not find file")
                driver.close()
                driver.quit()
        except:
            pass

    def clickCookie(self):
        driver = self.driver
        try:
            cookie = driver.find_element_by_id("bigCookie")
            cookie.click()
        except:
            options = driver.find_element_by_id("prefsButton")
            options.click()

    def buyGrandma(self):
        driver = self.driver
        try:
            grandma = driver.find_element_by_xpath("//div[@id='product1'][@class='product unlocked enabled']")
            grandma.click()
            self.buyFlag = 1
            print("buyFlag: " + str(self.buyFlag))
        except:
            self.buyFlag = 0
            print("buyFlag: " + str(self.buyFlag))

    def buyFarm(self):
        driver = self.driver
        try:
            farm = driver.find_element_by_xpath("//div[@id='product2'][@class='product unlocked enabled']")
            farm.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyMine(self):
        driver = self.driver
        try:
            mine = driver.find_element_by_xpath("//div[@id='product3'][@class='product unlocked enabled']")
            mine.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyFactory(self):
        driver = self.driver
        try:
            factory = driver.find_element_by_xpath("//div[@id='product4'][@class='product unlocked enabled']")
            factory.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyBank(self):
        driver = self.driver
        try:
            bank = driver.find_element_by_xpath("//div[@id='product5'][@class='product unlocked enabled']")
            bank.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyTemple(self):
        driver = self.driver
        try:
            temple = driver.find_element_by_xpath("//div[@id='product6'][@class='product unlocked enabled']")
            temple.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyWizardTower(self):
        driver = self.driver
        try:
            wizardTower = driver.find_element_by_xpath("//div[@id='product7'][@class='product unlocked enabled']")
            wizardTower.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyShipment(self):
        driver = self.driver
        try:
            shipment = driver.find_element_by_xpath("//div[@id='product8'][@class='product unlocked enabled']")
            shipment.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyAlchemyLab(self):
        driver = self.driver
        try:
            alchemyLab = driver.find_element_by_xpath("//div[@id='product9'][@class='product unlocked enabled']")
            alchemyLab.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyPortal(self):
        driver = self.driver
        try:
            portal = driver.find_element_by_xpath("//div[@id='product10'][@class='product unlocked enabled']")
            portal.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyTimeMachine(self):
        driver = self.driver
        try:
            timeMachine = driver.find_element_by_xpath("//div[@id='product11'][@class='product unlocked enabled']")
            timeMachine.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyAntimatterCondenser(self):
        driver = self.driver
        try:
            antimatterCondenser = driver.find_element_by_xpath("//div[@id='product12'][@class='product unlocked enabled']")
            antimatterCondenser.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyPrism(self):
        driver = self.driver
        try:
            prism = driver.find_element_by_xpath("//div[@id='product13'][@class='product unlocked enabled']")
            prism.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyChancemaker(self):
        driver = self.driver
        try:
            chancemaker = driver.find_element_by_xpath("//div[@id='product14'][@class='product unlocked enabled']")
            chancemaker.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def buyFractalEngine(self):
        driver = self.driver
        try:
            fractalEngine = driver.find_element_by_xpath("//div[@id='product15'][@class='product unlocked enabled']")
            fractalEngine.click()
            self.buyFlag = 1
        except:
            self.buyFlag = 0

    def closeAchievement(self):
        driver = self.driver
        try:
            close = driver.find_element_by_xpath("//div[@class='close']")
            close.click()
        except:
            pass

    def checkCookies(self):
        driver = self.driver
        try:
            cookieTemp = driver.find_element_by_xpath("//div[@id='cookies']").text
            number = cookieTemp[:cookieTemp.index(" ")]
            multiplier = cookieTemp[cookieTemp.index(" "):]
            multiplier = multiplier[1:]
            multiplier = multiplier[:multiplier.index("\n")]
            if multiplier == 'cookies' or multiplier == 'cookie':
                try:
                    a = number[:number.index(",")]
                    b = number[number.index(","):]
                    b = b[1:]
                    cookieTemp = int(a+b)
                except:
                    cookieTemp = int(number)
            elif multiplier == 'million':
                cookieTemp = float(number)
                cookieTemp = cookieTemp*math.pow(10, 6)
            elif multiplier == 'billion':
                cookieTemp = float(number)
                cookieTemp = cookieTemp*math.pow(10, 9)
            elif multiplier == 'trillion':
                cookieTemp = float(number)
                cookieTemp = cookieTemp*math.pow(10, 12)
            elif multiplier == 'quadrillion':
                cookieTemp = float(number)
                cookieTemp = cookieTemp*math.pow(10, 15)
            self.cookiesNum = cookieTemp
        except:
            pass

    def clickGoldenCookie(self):
        driver = self.driver
        try:
            goldenCookie = driver.find_element_by_xpath("//div[@class='shimmer']")
            goldenCookie.click()
        except:
            pass

    def buyUpgrade(self):
        driver = self.driver
        try:
            upgrade = driver.find_element_by_xpath("//div[@class='crate upgrade enabled']")
            upgrade.click()
            print("Upgrade!")
        except:
            pass


###################################
########## MAIN PROGRAM ###########
###################################

#Start bot and load page
cookieMonster = cookieBot()
cookieMonster.openCookieClicker()
cookieMonster.loadFile()
time.sleep(1)

#Define timers
def checkCookiesTimer():
    while(1):
        time.sleep(5)
        cookieMonster.checkCookies()
        cookieMonster.closeAchievement()
        # print("Cookies#: " + str(cookieMonster.cookiesNum))

def checkTime():
    while(1):
        if cookieMonster.buyFlag:
            cookieMonster.startTime = time.time()
            print("toggled")
            time.sleep(0.1)
        else:
            cookieMonster.endTime = time.time()

#Start timers
t1 = threading.Thread(target=checkCookiesTimer)
t1.start()
t2 = threading.Thread(target=checkTime)
t2.start()
time.sleep(2)

cookieMonster.startTime = time.time() #Start counting

#Stages
while(cookieMonster.flag <= len(objectives)):
    while(cookieMonster.cookiesNum < objectives[cookieMonster.flag]):
        # print(cookieMonster.endTime - cookieMonster.startTime)

        if cookieMonster.endTime - cookieMonster.startTime >= 180:
            cookieMonster.buyUpgrade()
            cookieMonster.startTime = time.time()

        cookieMonster.clickCookie()
        cookieMonster.clickGoldenCookie()

        if cookieMonster.flag == 1:
            cookieMonster.buyGrandma()
        elif cookieMonster.flag == 2:
            cookieMonster.buyFarm()
        elif cookieMonster.flag == 3:
            cookieMonster.buyMine()
        elif cookieMonster.flag == 4:
            cookieMonster.buyFactory()
        elif cookieMonster.flag == 5:
            cookieMonster.buyBank()
        elif cookieMonster.flag == 6:
            cookieMonster.buyTemple()
        elif cookieMonster.flag == 7:
            cookieMonster.buyWizardTower()
        elif cookieMonster.flag == 8:
            cookieMonster.buyShipment()
        elif cookieMonster.flag == 9:
            cookieMonster.buyAlchemyLab()
        elif cookieMonster.flag == 10:
            cookieMonster.buyPortal()
        elif cookieMonster.flag == 11:
            cookieMonster.buyTimeMachine()
        elif cookieMonster.flag == 12:
            cookieMonster.buyAntimatterCondenser()
        elif cookieMonster.flag == 13:
            cookieMonster.buyPrism()
        elif cookieMonster.flag == 14:
            cookieMonster.buyChancemaker()
        elif cookieMonster.flag == 15:
            cookieMonster.buyFractalEngine()
        else:
            pass

    cookieMonster.flag = cookieMonster.flag + 1
