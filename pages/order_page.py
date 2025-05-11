import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):

    @allure.step("Заполнить поля в первой форме")
    def fill_first_form_fields(self, first_name, last_name, station_index, address, phone):
        self.send_keys_to_input(OrderPageLocators.FIRST_NAME, first_name)
        self.send_keys_to_input(OrderPageLocators.LAST_NAME, last_name)
        self.send_keys_to_input(OrderPageLocators.ADDRESS, address)
        self.send_keys_to_input(OrderPageLocators.PHONE, phone)
        self.click_on_element(OrderPageLocators.METRO_STATION)
        self.click_on_element(OrderPageLocators.choose_station(station_index))
        self.click_on_element(OrderPageLocators.CONTINUE)

    @allure.step("Заполнить поля во второй форме")
    def fill_second_form_fields(self, date_day, duration, colour, comment):
        self.send_keys_to_input(OrderPageLocators.DATE_OF_START, date_day)
        self.click_on_element(OrderPageLocators.RENT_DURATION)
        self.click_on_element(OrderPageLocators.choose_rent_duration(duration))
        self.click_on_element(OrderPageLocators.choose_colour(colour))
        self.send_keys_to_input(OrderPageLocators.COMMENT, comment)

    @allure.step("Подтвердить заказ")
    def accept_order(self):
        self.click_on_element(OrderPageLocators.ORDER_BUTTON)
        self.click_on_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_order_message(self):
        self.get_text_on_element(OrderPageLocators.SUCCESS_ORDER_MESSAGE_FORM)

    @allure.step("Кликнуть на лого Самоката")
    def click_on_samokat_logo(self):
        self.click_on_element(OrderPageLocators.SAMOKAT_LOGO_BUTTON)

    @allure.step("Кликнуть на лого Яндекса")
    def click_on_ya_logo(self):
        self.click_on_element(OrderPageLocators.YA_LOGO_BUTTON)
