import time
import pytest
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.logger()  # Logger

    def test_SearchCustomerByEmail(self, setup):
        self.logger.info("**** SearchCustomerByEmail_004 ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successful *****")

        self.logger.info("***** searching customer by Email *****")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.clickOnCustomersMenu()
        self.add_cust.clickOnCustomersMenuItem()

        self.logger.info("***** searching customer by emailID ****")
        search_cust = SearchCustomer(self.driver)
        search_cust.setEmail("victoria_victoria@nopCommerce.com")
        search_cust.clickSearch()
        time.sleep(5)
        status=search_cust.searchCustomerByEmail("victoris_victoria@nopCommerce.com")
        assert True==status
        self.logger.info("****** TC_SearchCustomerBYEmail_004 Finished ****")

        self.driver.close()