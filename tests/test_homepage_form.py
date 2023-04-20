import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestForm(BaseClass):

    def test_form_submission(self, data):

        home_page = HomePage(self.driver)
        home_page.get_name_textbox().send_keys(data["name"])
        home_page.get_email_textbox().send_keys(data["email"])
        home_page.get_password_textbox().send_keys(data["password"])
        home_page.get_gender_list(data["gender"])

        radios = home_page.get_employment_radios()
        for count, option in enumerate(radios):
            if option.text == data["emp_status"].title():
                radios[count].click()

        home_page.get_date_textbox().send_keys(data["date"])
        home_page.get_submit_button().click()
        message = home_page.get_success_message().text

        assert ("Success!" in message)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_form_data)
    def data(self, request):
        return request.param
