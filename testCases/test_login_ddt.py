import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customlogger import logGen
from utilities import XLUtils

class test_002_DDT_Login:
    baseURL =ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"
     logger=logGen.loggen()

            def test_login_ddt(self,setup):
                self.logger.info("********* Test_002_DDT_Login ******")
                self.logger.info("**************** Verifying Login Test ***************")
                self.driver = setup
                self.driver.get(self.baseURL)

                self.lp=loginPage(self.driver)

            self.rows=XLUtils.getRowCount(self.path,'sheet1')
    print("Number of Rows i a Excel:",self.rows)

    for r in range(2,self.rows+1):
        self.userXLUtils.readData(self.path,'sheet1',r,1)
        self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
        self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)

        self.lpsetuserName(self.user)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(5)

        act_title=self.driver.title
        exp_title="Dashboard / nopCommerce administration"






                self.lp.setUserName(self.UserName)
                self.lp.setPassword(self.Password)
                self.lp.clicklogin()
                act_title=self.driver.title

                if act_title=="<title>Dashboard / nopCommerce administration</title>"
                    assert True
                    self.logger.info("**************** Login test case passed ***************")
                    self.driver.Close()
                esle:
                    self.driver.save_screenshot(".\\screenshot\\"+"test_login.png")
                    self.driver.Close()
                self.logger.info("**************** Login test case failed***************")
                    assert False



