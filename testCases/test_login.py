import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen



class test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger=LogGen.logger()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("********** Test_001_Login *****")
        self.logger.info("********** Verifying Home page Title *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Verifying Home page title test is passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" +"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Verifying Home page title test is failed *****")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********** Verifying Login Test *****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Login test is passed *****")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********** Login test is failed *****")
            assert False




