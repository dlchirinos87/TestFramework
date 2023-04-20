from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.ShopPage import ShopPage


class HomePage:
    """Contains elements in homepage."""
    def __init__(self, driver):
        self.driver = driver

    shop_button_locator = (By.CSS_SELECTOR, "a[href*='shop']")
    name_textbox_locator = (By.CSS_SELECTOR, "div[class='form-group'] input[name='name']")
    email_textbox_locator = (By.NAME, "email")
    password_textbox_locator = (By.ID, "exampleInputPassword1")
    checkbox_locator = (By.CSS_SELECTOR, "#exampleCheck1")
    gender_list_locator = (By.ID, "exampleFormControlSelect1")
    employment_radio_locators = (By.CLASS_NAME, "form-check-inline")
    date_locator_textbox = (By.CSS_SELECTOR, "input[name='bday']")
    submit_button_locator = (By.CSS_SELECTOR, "input[value='Submit']")
    success_message_locator = (By.CLASS_NAME, "alert-dismissible")


    def click_shop_page_button(self):
        """Clicks shop button to proceed to shop page and returns object for shop page."""
        self.driver.find_element(*HomePage.shop_button_locator).click()
        shop_page = ShopPage(self.driver)
        return shop_page

    def get_name_textbox(self):
        return self.driver.find_element(*HomePage.name_textbox_locator)

    def get_email_textbox(self):
        return self.driver.find_element(*HomePage.email_textbox_locator)

    def get_password_textbox(self):
        return self.driver.find_element(*HomePage.password_textbox_locator)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox_locator)

    def get_gender_list(self, gender):
        gender_dropdown = Select(self.driver.find_element(*HomePage.gender_list_locator))
        gender_dropdown.select_by_visible_text(gender)

    def get_employment_radios(self):
        return self.driver.find_elements(*HomePage.employment_radio_locators)

    def get_date_textbox(self):
        return self.driver.find_element(*HomePage.date_locator_textbox)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button_locator)

    def get_success_message(self):
        return self.driver.find_element(*HomePage.success_message_locator)
