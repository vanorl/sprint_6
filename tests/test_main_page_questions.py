import allure
import pytest

import data
from pages.main_page import MainPage


class TestQuestions:
    @allure.title("Проверка ответов на вопросы о важном")
    @pytest.mark.parametrize('question_number, expected_answer', data.Data.answers)
    def test_answers(self, driver, question_number, expected_answer):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_question(question_number)
        answer = main_page.take_answer(question_number)
        assert main_page.get_text_on_element(answer) == expected_answer, 'Ответ не соответствует ожидаемому'
