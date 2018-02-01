import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTests (unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome("/Users/sulemandaud/Downloads/chromedriver")
        # cls.driver = webdriver.Chrome("F:\chromedriver")
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        cls.driver.get("https://secure.swipedon.com")
        cls.email_field = cls.driver.find_element_by_name("login-email")
        cls.email_field.clear()
        cls.email_field.send_keys("lts@lts.com")
        cls.pass_field = cls.driver.find_element_by_name("login-password")
        cls.pass_field.clear()
        cls.pass_field.send_keys("123456")
        cls.driver.implicitly_wait(3)
        cls.btn_submit = cls.driver.find_element_by_id("login-submit")
        cls.btn_submit.submit()

    def test_login(self):
        self.driver.implicitly_wait(30)

        assert "Dashboard" in self.driver.page_source

        # self.driver.find_element_by_link_text('Employees').click()

    def test_employee_link(self):
        employee = self.driver.find_element_by_link_text('Employees')
        employee.click()

        assert "Your most important asset" in self.driver.page_source
        self.driver.back()

    def test_visitor_link(self):
        visitors = self.driver.find_element_by_id('vis-main-menu')
        visitors.click()

        assert "Know exactly who's in" in self.driver.page_source
        self.driver.back()

    def test_evacuation_link(self):
        self.driver.find_element_by_xpath("//a[@href='/evacuation']").click()

        assert "Know exactly who's in" in self.driver.page_source
        self.driver.back()

    def test_prereg_link(self):
        self.driver.find_element_by_xpath("//a[@href='/preRegistration']").click()

        assert "Because First Impressions Last" in self.driver.page_source
        self.driver.back()

    def test_admin_link(self):
        self.driver.find_element_by_xpath("//a[@href='/companiesAdmins']").click()

        assert  "Manage the powered ones" in self.driver.page_source
        self.driver.back()

    def test_setting_bnd_link(self):
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        self.driver.find_element_by_xpath("//a[@href='/settings/branding-and-design']").click()
        assert "Branding and Design" in self.driver.page_source

    def test_setting_pnp_link(self):
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        self.driver.find_element_by_xpath("//a[@href='/settings/photo-id-printing']").click()
        assert "Photo and ID Printing" in self.driver.page_source

    def test_setting_pnp_link(self):
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        self.driver.find_element_by_xpath("//a[@href='/settings/visitor-fields']").click()
        assert "Visitor Fields" in self.driver.page_source

    def test_setting_agree_link(self):
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        self.driver.find_element_by_link_text('Visitor Agreement').click()
        assert "Agreement Settings" in self.driver.page_source

    def test_setting_vissetings_link(self):
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        self.driver.find_element_by_xpath("//a[@href='/settings/visitor-settings']").click()
        assert "Visitor Settings" in self.driver.page_source

    def test_setting_notificationsettings_link(self):
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        self.driver.find_element_by_xpath("//a[@href='/settings/notification-settings']").click()
        assert "Notification Settings" in self.driver.page_source

    def test_setting_empsettings_link(self):
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        self.driver.find_element_by_xpath("//a[@href='/settings/employee']").click()
        assert "Employee Settings" in self.driver.page_source

    def test_setting_ipadnlocations_link(self):
        self.driver.find_element_by_xpath("//a[@href='/settings']").click()
        self.driver.find_element_by_xpath("//a[@href='/settings/ipads-locations']").click()
        assert "iPads and Locations" in self.driver.page_source

    def test_account_companyname_link(self):
            self.driver.find_element_by_link_text('Account').click()
            self.driver.find_element_by_xpath("//a[@href='/billing/company-info']").click()

            #self.driver.find_element_by_xpath("//a[@href='/settings/ipads-locations']").click()
            assert "Company Info" in self.driver.page_source

    def test_account_planpricing_link(self):
        self.driver.find_element_by_link_text('Account').click()
        self.driver.find_element_by_xpath("//a[@href='/billing/plans-and-pricing']").click()

        # self.driver.find_element_by_xpath("//a[@href='/settings/ipads-locations']").click()
        assert "Simple Pricing" in self.driver.page_source

    def test_account_smsbilling_link(self):
        self.driver.find_element_by_link_text('Account').click()
        self.driver.find_element_by_link_text('Plans and Pricing').click()

        # self.driver.find_element_by_xpath("//a[@href='/settings/ipads-locations']").click()
        assert "SMS Billing Transactions" in self.driver.page_source

    def test_account_planbilling_link(self):
        self.driver.find_element_by_link_text('Account').click()
        self.driver.find_element_by_link_text('Plans and Pricing').click()

        # self.driver.find_element_by_xpath("//a[@href='/settings/ipads-locations']").click()
        assert "Billing Transactions" in self.driver.page_source




    #def test_billing_link(self):
    #    self.driver.find_element_by_partial_link_text('Account').click()
     #   self.driver.implicitly_wait(30)
      #  self.driver.find_element_by_xpath("//a[@href='/billing/plans-and-pricing']").click()

       # assert "Fair Pricing, Flexible Plans. Packed with Features" in self.driver.page_source


    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)