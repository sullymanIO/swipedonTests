import unittest
from selenium import webdriver

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
        employee = self.driver.find_element_by_id('emp-main-menu')
        employee.click()

        assert "Your most important asset" in self.driver.page_source

    @classmethod
    def tearDownClass(cls):
         cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)