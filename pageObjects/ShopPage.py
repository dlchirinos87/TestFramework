from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage


class ShopPage:
    """Contains elements in Shop Page."""
    def __init__(self, driver):
        self.driver = driver

    products_titles_locators = (By.CSS_SELECTOR, ".card-title a")
    products_buttons_locators = (By.CSS_SELECTOR, ".card-footer button")
    checkout_button_locator = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def get_products_titles(self):
        """Returns locators of all products' titles currently present in the shop page."""
        return self.driver.find_elements(*ShopPage.products_titles_locators)

    def get_products_buttons(self):
        """Returns locators of all products' buttons currently present in the shop page."""
        return self.driver.find_elements(*ShopPage.products_buttons_locators)

    def click_checkout_button(self):
        """Clicks checkout button to proceed to checkout page and returns object for checkout page."""
        self.driver.find_element(*ShopPage.checkout_button_locator).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
