import allure

from pages.order_page import OrderPage
from urls import main_site, dzen_site


class TestNavigateButtons:
    @allure.step("Проверить переход на главную при клике на лого Самоката")
    def test_click_samokat_logo_navigates_to_main_site(self, order_driver):
        navigate_button = OrderPage(order_driver)
        navigate_button.click_on_samokat_logo()
        assert order_driver.current_url == main_site, 'Текущий url не соответствует ожидаемому'

    @allure.step("Проверить открытие в новом окне главной страницы Дзена при клике на лого Яндекса")
    def test_click_yandex_logo_open_dzen_site_in_new_tab(self, order_driver):
        navigate_button = OrderPage(order_driver)
        navigate_button.click_on_ya_logo()
        navigate_button.switch_and_get_url()
        assert order_driver.current_url == dzen_site, 'Текущий url не соответствует ожидаемому'
