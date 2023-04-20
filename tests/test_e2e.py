import pytest

from TestData.e2eData import E2eData
from utilities.BaseClass import BaseClass
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):
    """End to End test cases for https://rahulshettyacademy.com/angularpractice/ website"""

    def test_e2e(self, data):
        """a happy path test for rahulshettyacademy.com website"""

        home_page = HomePage(self.driver)

        shop_page = home_page.click_shop_page_button()

        products = shop_page.get_products_titles()
        for count, product in enumerate(products):
            if product.text == data['item']:
                shop_page.get_products_buttons()[count].click()

        checkout_page = shop_page.click_checkout_button()

        confirm_page = checkout_page.get_checkout_button()
        confirm_page.get_location_textbox().send_keys(data['suggestion'])
        self.dropdown_list_is_present(data['selected_country'])
        confirm_page.get_country_dropdown_list(data['selected_country']).click()
        confirm_page.get_checkbox().click()
        confirm_page.get_purchase_button().click()
        message = confirm_page.get_success_message().text

        assert ("Success!" in message)

        self.driver.refresh()

    @pytest.fixture(params=E2eData.test_e2e_data)
    def data(self, request):
        return request.param
