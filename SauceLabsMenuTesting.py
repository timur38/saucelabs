# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class SauceLabsHeaders(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://saucelabs.com/"
        self.verificationErrors = []
    
    def test_sauce_labs_headers(self):
        driver = self.driver
        driver.maximize_window()

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector(".bottom a[href='https://saucelabs.com/features']").click()
        try: self.assertRegexpMatches(driver.title, r"Features")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector(".bottom a[href='https://saucelabs.com/our-values']").click()
        try: self.assertRegexpMatches(driver.title, r"Values")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector("a[title='Community']").click()
        try: self.assertRegexpMatches(driver.title, r"Sause")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector("a[title='Solutions']").click()
        try: self.assertRegexpMatches(driver.title, r"Selenium")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector("a[title='Resources']").click()
        try: self.assertRegexpMatches(driver.title, r"Resources")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector(".pull-left a[title='Enterprise']").click()
        try: self.assertRegexpMatches(driver.title, r"Enterprise")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector("a[title='Sign up']").click()
        try: self.assertRegexpMatches(driver.title, r"Sign")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector(".pull-right a[title='Docs']").click()
        try: self.assertRegexpMatches(driver.title, r"Docs")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector(".pull-right a[title='Pricing']").click()
        try: self.assertRegexpMatches(driver.title, r"Pricing")
        except AssertionError as e: self.verificationErrors.append(str(e))

        driver.get(self.base_url)
        driver.find_element_by_css_selector(".hamburger").click()
        driver.find_element_by_css_selector("a[title='Log in']").click()
        try: self.assertRegexpMatches(driver.title, r"Log")
        except AssertionError as e: self.verificationErrors.append(str(e))

       
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
