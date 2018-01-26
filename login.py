import time
#from selenium import webdriver

#driver = webdriver.Chrome('/Users/sulemandaud/Downloads/chromedriver')  # Optional argument, if not specified will search path.
#driver.get('https://secure.swipedon.com');
#driver.fullscreen_window()
#time.sleep(5) # Let the user actually see something!
#email = driver.find_element_by_name('login-email')
#password = driver.find_element_by_id('login-password')
#email.send_keys('lts@lts.com')
#password.send_keys('123456')
#login = driver.find_element_by_id('login-submit')
#login.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()
import unittest
from selenium import webdriver


class SearchTests (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('/Users/sulemandaud/Downloads/chromedriver')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        self.driver.get("https://secure.swipedon.com")

    def test_search_by_category(self):
        self.email_field = self.driver.find_element_by_name("login-email")
        self.email_field.clear()
        self.email_field.send_keys("lls@lts.com")
        self.pass_field = self.driver.find_element_by_name("login-password")
        self.pass_field.clear()
        self.pass_field.send_keys("123456")
        self.btn_submit = self.driver.find_element_by_id("login-submit")
        self.btn_submit.submit()
        self.driver.implicitly_wait(30)

        assert "Dashboard" in self.driver.page_source


    def tearDown(self):
         self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
