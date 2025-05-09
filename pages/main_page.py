import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step("Кликнуть принять куки")
    def accept_cookies(self):
        self.click_on_element(MainPageLocators.ACCEPT_COKIES_BUTTON)


    @allure.step("Кликнуть на Заказать в шапке")
    def click_header_order_button(self):
        self.click_on_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Кликнуть на Заказать в теле")
    def click_body_order_button(self):
        self.scroll_to_element(MainPageLocators.BODY_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.BODY_ORDER_BUTTON)

    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_on_element(MainPageLocators.YA_LOGO_BUTTON)

    @allure.step("Нажать на логотип самоката")
    def click_samokat_logo(self):
        self.click_on_element(MainPageLocators.SAMOKAT_LOGO_BUTTON)

    @allure.step("Нажать на вопрос")
    def click_question(self, question_number):
        question_locator = MainPageLocators.question_number(question_number)
        self.scroll_to_element(MainPageLocators.QUESTIONS)
        self.click_on_element(question_locator)

    @allure.step("Получить текст ответа на вопрос")
    def take_answer(self, question_number):
        return MainPageLocators.answer(question_number)
