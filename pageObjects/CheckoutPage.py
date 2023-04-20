from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:
    """Contains elements in Checkout Page."""
    def __init__(self, driver):
        self.driver = driver

    checkout_button_locator = (By.XPATH, "//button[@class='btn btn-success']")

    def get_checkout_button(self):
        """Clicks checkout button to proceed to confirm page and returns object for confirm page."""
        self.driver.find_element(*CheckoutPage.checkout_button_locator).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
