import allure
import pytest

import data
from pages.order_page import OrderPage


class TestOrderScooter:
    @allure.description("Проверка заказа самоката")
    @pytest.mark.parametrize('first_name, last_name, metro_station, address, phone, date_day, duration, colour, comment', data.Data.order_data)
    def test_order_samokat_got_success_order_message(self, order_driver, first_name, last_name, metro_station, address, phone, date_day, duration, colour, comment):
        order_samokat = OrderPage(order_driver)
        order_samokat.fill_first_form_fields(first_name, last_name, metro_station, address, phone)
        order_samokat.fill_second_form_fields(date_day, duration, colour, comment)
        order_samokat.accept_order()
        assert order_samokat.get_success_order_message() == data.Data.success_order_message, 'Не удалось получить сообщение об успешном заказе'

