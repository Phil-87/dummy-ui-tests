from selenium.webdriver.common.by import By
from uitestcore.page import BasePage
from uitestcore.page_element import PageElement


class SimpleTestPage(BasePage):
    endpoint = ""
    expected_element = PageElement(By.XPATH, "//h1[contains(.,'Overview')]")

    def go_to_page(self, base_url):
        self.interact.open_url(base_url + self.endpoint)

    def expected_element_is_visible(self):
        return self.interrogate.is_element_visible(self.expected_element)
