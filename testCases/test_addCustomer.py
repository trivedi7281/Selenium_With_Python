import time
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readproperties import ReadConfig
from utilities.customLogger import LogGen
import string
import random


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.Loggen()  # Logger

    @pytest.mark.regression
    def test_addCustomer(self, setup):
        self.logger.info("**** Test_003_AddCustomer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successful *****")

        self.logger.info("***** Starting Add Customer Test *****")

        self.add_cust = AddCustomer(self.driver)
        self.add_cust.clickOnCustomerMenu()
        self.add_cust.clickOnCustomersMenuItem()

        self.add_cust.clickOnAddnew()

        self.logger.info("***** Providing customer info ****")

        self.email = random_generator() + "@gmail.com"
        self.add_cust.setEmail(self.email)
        self.add_cust.setPassword("test123")
        self.add_cust.setCustomerRoles("Guests")
        self.add_cust.setManagerOfVendor("Vendor")
        self.add_cust.setGender("Male")
        self.add_cust.setFirstName("Preeti")
        self.add_cust.setLastName("Chandrawat")
        self.add_cust.setDob("16/01/1997")
        self.add_cust.setCompanyName("busyQA")
        self.add_cust.setAdminContent("This is for testing....")
        self.add_cust.clickOnSave()

        self.logger.info("****** saving customer info ****")

        self.logger.info("**** Add customer validation ****")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("******* Add Customer Test Passed *****")
        else:
            self.driver.save_screenshot(".\\Screenshot\\" + "test_addCustomer_scr.png")
            self.logger.error("***** Add Customer Test Failed *****")
            assert True == False
            self.driver.close()
            self.logger.info("***** Ending Home Page test *****")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
