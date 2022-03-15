import pytest
import self
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.logger()

    @pytest.mark.regression
    def test_login_ddt(self, setup, lst_status=None):
        self.logger.info("********* Test_002_DDT_Login ******")
        self.logger.info("**************** Verifying Login Test ***************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = Login(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'sheet1')
        print("Number of Rows i a Excel:", self.rows)

        lst_status   # Empty List Variable

        for r in range(2, self.rows + 1):
            self.userXLUtils.readData(self.path, 'sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)

        self.lp.setuserName(self.user)
        self.lp.setPassword(self.password)
        self.lp.clicklogin()
        time.sleep(5)

        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"
        if act_title == exp_title:
            if self.exp == "Pass":
                self.logger.info("*** Passed")
                self.lp.clickLogout();
                lst_status.append("Pass")
            elif self.exp == "Fail":
                self.looger.info("**** failed***")
                self.lp.clcikLogout();
                lst_status.append("Fail")
        elif act_title != exp_title:
            if self.exp == "Pass":
                self.logger.info("*** failed")
                lst_status.append("Fail")
            elif self.exp == "Fail":
                self.looger.info("**** Passed ***")
                self.lp.clcikLogout();
                lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT test Passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test failed ***")
            self.driver.close()
            assert False

        self.logger.info("*** End of the Login DDT Test ****")
        self.logger.info("********* Completed TC_LoginDDT_002 *****")
