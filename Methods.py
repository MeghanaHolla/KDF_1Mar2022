import time

import allure
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Methods_List():
    driver = None
    def openApplication(self,url):
        global driver
        ser = Service("D:\Training\Selenium\Drivers\chromedriver.exe")
        self.driver = webdriver.Chrome(service=ser)
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(url)

    def enterInTextBox(self,loc,locValue,testdata):
        if(loc == "id"):
            self.driver.find_element(By.ID,locValue).send_keys(testdata)
        if(loc == "cssSelector"):
            self.driver.find_element(By.CSS_SELECTOR, locValue).send_keys(testdata)
        if (loc == "name"):
            self.driver.find_element(By.NAME, locValue).send_keys(testdata)

    def clickAButton(self,locValue):
        self.driver.find_element(By.NAME,locValue).click()

    def clickALink(self,locValue):
        count = 1
        while (True):
            try:
                self.driver.find_element(By.LINK_TEXT, locValue).click()
                break
            except:
                time.sleep(2)
                count = count + 1
                if count == 6:
                    print("script failed")
                    break;
                continue

    def scrollDown(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

    def hitKeyboardButton(self,loc,locValue,key):
        if(loc == "cssSelector"):
            if(key == "ENTER"):
                self.driver.find_element(By.CSS_SELECTOR,locValue).send_keys(Keys.ENTER)
            if(key == "TAB"):
                self.driver.find_element(By.CSS_SELECTOR, locValue).send_keys(Keys.TAB)
        if(loc == "name"):
            if (key == "ENTER"):
                self.driver.find_element(By.NAME, locValue).send_keys(Keys.ENTER)
            if (key == "TAB"):
                self.driver.find_element(By.NAME, locValue).send_keys(Keys.TAB)

    def clickWebElement(self,locValue):
        self.driver.find_element(By.CSS_SELECTOR,locValue).click()

    def selectValueFromDropdown(self,locValue,testData):
        dd = self.driver.find_element(By.NAME,locValue)
        ddObj = Select(dd)
        ddObj.select_by_visible_text(testData)

    def getText(self,locValue):
        return self.driver.find_element(By.CSS_SELECTOR,locValue).text

    def closeApplication(self):
        self.driver.close()