class SearchCustomer:
    # Add customer Page
    txt_Email_id = "SearchEmail"
    txt_FirstName_id = "SearchFirstName"
    txt_LastName_id = "SearchLastName"
    btn_Search_id = "search_customers"

    tblSearchResults_xpath = "//table[@role='grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_id(self.txt_Email_id).clear()
        self.driver.find_element_by_id(self.txt_Email_id).send_keys(email)

    def setFirstName(self, firstName):
        self.driver.find_element_by_id(self.txt_FirstName_id).clear()
        self.driver.find_element_by_id(self.txt_FirstName_id).send_keys(firstName)

    def setLastName(self, lastName):
        self.driver.find_element_by_id(self.txt_LastName_id).clear()
        self.driver.find_element_by_id(self.txt_LastName_id).send_keys(lastName)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btn_Search_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elemeny_by_xpath(self.tableRows_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(
                "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[2]").text()
            if table == email:
                flag = True
                break
            return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(
                "//table[@id='customers-grid']/tbody/tr[" + str(r) + "]/td[3]").text()
            if table == Name:
                flag = True
                break
            return flag
