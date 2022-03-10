from selenium import webdriver
import pytest
# updated....

from pageobjects.LoginPage import LoginPage
from utilities.readproproties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getuserEmail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self,setup):   # to verify homepage title
        self.logger.info("**********Test_001_Login*************")
        self.logger.info("**********Verifying Home Page Title*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************Home Page Title is Passed**************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************Home Page Title is failed**************")
            assert False

    def test_login(self,setup):
        self.logger.info("***********Verifying Login Test************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)   # create object for LoginPage by using self.lp we call the pageobjects
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***********Login Test is Passed************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("***********Login Test is failed************")
            assert False







