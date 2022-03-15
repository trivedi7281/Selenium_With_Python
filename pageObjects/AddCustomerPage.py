import time
from selenium.webdriver.support.ui import Select


class AddCustomer:

# Add customer Page
lnk_Customer_menu_xpath = "//a[@href='#']//span[contains(text(),'Customers')]"
lnk_Customer_menuItem_xpath = "//span[@cclas='menu-item-title'][contains(text(),'Customers')]"
btn_AddNew_xpath = "//a[@class='btn bg-blue']"
txt_Email_xpath = "//input[@id='Password']"
txt_customerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
lst_itemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
lst_itemRegistered_xpath = "//li[contains(text(),'Registered')]"
lst_itemGuests_xpath = "//li[contains(text(),'Guests')]"
lst_itemVendors_xpath = "//li[contains(text(),'Vendors')]"
drp_mgrOfVendor_xpath = "//*[@id='VendorID')]"
rd_MaleGender_id = "Gender_Male"
rd_FeMaleGender_id = "Gender_Female"
txt_FirstName_xpath = "//input[@id='FirstName']"
txt_LastName_xpath = "//input[@id='LastName']"
txt_Dob_xpath = "//input[@id='DateOfBirth']"
txt_CompanyName_xpath = "//input[@id='Company']"
txt_AdminContent_xpath = "//textarea[@id='AdminComment']"
btnSave_xpath = "//button[@name='save']"


def __init__(self, driver):
    self.driver = driver


def clickOnCustomersMenu(self):
    self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()


def clickOnCustomersMenuItem(self):
    self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()


def clcikOnAddnew(self):
    self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()


def setEmail(self, email):
    self.driver.find_element_by_xpath(self.txtEmail_xpath).send_Keys(email)


def setpassword(self, password):
    self.driver.find_element_by_xpath(self.txtPassword_xpath).send_Keys(password)


def setCustomerRoles(self, role):
    self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
    time.sleep(3)
    if role == 'Registered':
        self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
    elif role == 'Administrators':
        self.listitem = self.driver.find_element_by_xpath(self.lstitemAfministrators_xpath)
    elif role == 'Gusets':
        # Here use can be registered (or) Guest, only one
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[@id='selectdCustomersRolesIds_taglist']/lispan[2]").click()
        self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
    elif role == 'Registered':
        self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
    elif role == 'Vendors':
        self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
    else:
        self.listitem = self.driver.find_element_by_xpath(self.listitemVendors_xpath)
    time.sleep(3)
    # self.listitem.click();
    self.driver.excute_script("argument[0].click();", self.listitem)


def setManagertofVendor(self, value):
    drp = Select(self.driver.find_element_by_xpath(self.drpmgrVendor_xpath))
    drp.select_by_visible_text(value)


def setGender(self, gender):
    if gender == 'Male':
        self.driver.find_element_byid(self.rdMaleGender_id).click()
    elif gender == 'Female':
        self.driver.find_element_by_id(self.rdFeMaleGender_id).Click()
    else:
        self.driver.find_element_byid(self.rdMalkeGender_id).click()


def setFirstName(self, fName):
    self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fName)


def setLastName(self, lName):
    self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lName)


def setDob(self, dob):
    self.driver.find_element_by_xpath(self.txtdob_xpath).send_keys(dob)


def setCompanyName(self, comname):
    self.driver.find_element_by_xpath(self.txtcomname_xpath).send_keys(comname)


def setAdminContent(self, content):
    self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)


def clickOnSave(self):
    self.driver.find_element_by_xpath(self.btnSave_xpath).click()
