import unittest
from selenium import webdriver

class TestMskRtRu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://msk.rt.ru/")

    def test_home_page_title(self):
        self.assertEqual(self.driver.title, "Ростелеком")

    def test_home_page_header(self):
        self.assertIn("Интернет, ТВ и телефония", self.driver.find_element_by_xpath("//h1").text)

    def test_home_page_services(self):
        self.assertIn("Интернет", self.driver.find_element_by_xpath("//div[@class='col-md-6']//a[1]").text)
        self.assertIn("Телевидение", self.driver.find_element_by_xpath("//div[@class='col-md-6']//a[2]").text)
        self.assertIn("Телефония", self.driver.find_element_by_xpath("//div[@class='col-md-6']//a[3]").text)

    def test_home_page_contact_info(self):
        self.assertIn("8 800 100-0-800", self.driver.find_element_by_xpath("//div[@class='contact-info']//a[1]").text)
        self.assertIn("info@rt.ru", self.driver.find_element_by_xpath("//div[@class='contact-info']//a[2]").text)

    def test_internet_page(self):
        self.driver.find_element_by_xpath("//a[contains(text(), 'Интернет')]").click()
        self.assertEqual(self.driver.title, "Интернет от Ростелеком")
        self.assertIn("Скорость до 890 Мбит/с", self.driver.find_element_by_xpath("//h1").text)
        self.assertIn("Акция! Подключи интернет и получи 3 месяца в подарок", self.driver.find_element_by_xpath("//div[@class='promo-banner']//h2").text)

    def test_tv_page(self):
        self.driver.find_element_by_xpath("//a[contains(text(), 'Телевидение')]").click()
        self.assertEqual(self.driver.title, "Телевидение от Ростелеком")
        self.assertIn("286 каналов", self.driver.find_element_by_xpath("//h1").text)
        self.assertIn("Акция! Подключи ТВ и получи 2 месяца в подарок", self.driver.find_element_by_xpath("//div[@class='promo-banner']//h2").text)

    def test_phone_page(self):
        self.driver.find_element_by_xpath("//a[contains(text(), 'Телефония')]").click()
        self.assertEqual(self.driver.title, "Телефония от Ростелеком")
        self.assertIn("Домашний телефон", self.driver.find_element_by_xpath("//h1").text)
        self.assertIn("Акция! Подключи домашний телефон и получи скидку 50% на первые 3 месяца", self.driver.find_element_by_xpath("//div[@class='promo-banner']//h2").text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()