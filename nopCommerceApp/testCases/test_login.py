import time

from pageObjects.loginPage import Login
from utilitites.customLogger import LogGen
from utilitites.readProperties import readConfig


class Test_001_Login:
    baseURL = readConfig.getApplicationUrl()
    username = readConfig.getUserEmail()
    password = readConfig.getUserPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info("************** test_homePageTitle **************")
        self.logger.info("************** Verifying test_homePageTitle **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.driver.close()
            self.logger.info("************** Home page title is passed **************")
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("************** Home page title is failed **************")
            assert False

    def test_login(self, setup):
        self.logger.info("************** test_login **************")
        self.logger.info("************** Verifying test_login **************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        time.sleep(5)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************** dashboard title is passed **************")
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot("../Screenshots/" + "test_login.png")
            self.driver.close()
            self.logger.error("************** dashboard title is failed **************")
            assert False
