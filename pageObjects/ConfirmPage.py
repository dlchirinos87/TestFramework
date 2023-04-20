from selenium.webdriver.common.by import By


class ConfirmPage:
    """Contains elements in Confirm Page."""

    def __init__(self, driver):
        self.driver = driver

    dropdown_textbox_locator = (By.ID, "country")
    checkbox_locator = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase_button_locator = (By.CSS_SELECTOR, "[type='submit']")
    success_message_locator = (By.CLASS_NAME, "alert-dismissible")

    def get_location_textbox(self):
        return self.driver.find_element(*ConfirmPage.dropdown_textbox_locator)

    def get_country_dropdown_list(self, country):
        return self.driver.find_element(By.LINK_TEXT, country)

    def get_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox_locator)

    def get_purchase_button(self):
        return self.driver.find_element(*ConfirmPage.purchase_button_locator)

    def get_success_message(self):
        return self.driver.find_element(*ConfirmPage.success_message_locator)
