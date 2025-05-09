from selenium.webdriver.common.by import By

class MainPageLocators:
    HEADER_ORDER_BUTTON = [By.CLASS_NAME, 'Button_Button__ra12g'] #кнопка заказать в шапке
    BODY_ORDER_BUTTON = [By.CLASS_NAME, 'Button_UltraBig__UU3Lp'] #кнопка заказать в теле
    ACCEPT_COKIES_BUTTON = [By.CLASS_NAME, 'App_CookieButton__3cvqF'] #кнопка принять куки
    QUESTIONS = [By.CLASS_NAME, 'Home_FourPart__1uthg'] #раздел с вопросами
    SAMOKAT_LOGO_BUTTON = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']  # кнопка логотипа самоката
    YA_LOGO_BUTTON = [By.CLASS_NAME, 'Header_Logo__23yGT']  # кнопка логотипа яндекса

    @staticmethod
    def question_number(question_number):
        question = (By.ID , f"accordion__heading-{question_number}")
        return question

    @staticmethod
    def answer(question_number):
        answer = (By.XPATH, f"//div[@id='accordion__panel-{question_number}']/p")
        return answer