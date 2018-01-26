import unittest
from selenium import webdriver


class SearchTests (unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome("/Users/sulemandaud/Downloads/chromedriver")
       self.driver.implicitly_wait(30)
       self.driver.maximize_window()

       self.driver.get("https://secure.swipedon.com")
       self.email_field = self.driver.find_element_by_name("login-email")
       self.email_field.clear()
       self.email_field.send_keys("lts@lts.com")
       self.pass_field = self.driver.find_element_by_name("login-password")
       self.pass_field.clear()
       self.pass_field.send_keys("123456")
       self.driver.implicitly_wait(3)
       self.btn_submit = self.driver.find_element_by_id("login-submit")
       self.btn_submit.submit()

   def test_login(self):
       self.driver.implicitly_wait(30)

       assert "Dashboard" in self.driver.page_source

       # self.driver.find_element_by_link_text('Employees').click()

   def test_employee_link(self):
       employee = self.driver.find_element_by_id('emp-main-menu')
       employee.click()

       assert "Your most important asset" in self.driver.page_source
       #self.driver.navigate.back()

   def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
   unittest.main(verbosity=3)