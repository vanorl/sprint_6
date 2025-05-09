from selenium.webdriver.common.by import By

class OrderPageLocators:
    #поля первой формы
    FIRST_NAME = [By.XPATH, './/input[@placeholder = "* Имя"]'] #поле имя
    LAST_NAME = [By.XPATH, './/input[@placeholder = "* Фамилия"]'] #поле фамилия
    METRO_STATION = [By.XPATH, '//input[@class ="select-search__input"]'] #поле выбора станции метро
    METRO_STATION_VALUES = [By.XPATH, '//ul[@class="select-search__options"]'] #выпадающий список станций
    ADDRESS = [By.XPATH, './/input[@placeholder = "* Адрес: куда привезти заказ"]'] #поле адрес
    PHONE = [By.XPATH, './/input[@placeholder = "* Телефон: на него позвонит курьер"]'] #поле телефон

    CONTINUE = [By.XPATH, './/button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]']  #кнопка далее в первой форме

    #поля второй формы
    DATE_OF_START = [By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]'] #поле выбора даты
    RENT_DURATION = [By.XPATH, '//span[@class ="Dropdown-arrow"]'] #поле сроков аренды

    BLACK_SCOOTER = [By.ID, 'black'] #чекбокс черный цвет
    GREY_SCOOTER = [By.ID, 'grey'] #чекбокс серый цвет
    COMMENT = [By.XPATH, '//input[@placeholder ="Комментарий для курьера"]'] #поле коммент
    ORDER_BUTTON = [By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"])[1]'] #кнопка заказать в форме
    CONFIRM_ORDER_BUTTON = [By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"])[2]'] #кнопка подтвердить
    SUCCESS_ORDER_MESSAGE_FORM = [By.XPATH, '//div[@class ="Order_Modal__YZ-d3"]']  # окно с сообщением об успешном заказе
    CHECK_STATUS_BUTTON = [By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"])[2]'] #кнопка посмотреть статус

    SAMOKAT_LOGO_BUTTON = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR'] #кнопка логотипа самоката
    YA_LOGO_BUTTON = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI'] #кнопка логотипа яндекса

    @staticmethod
    def choose_station(station_index):
        return By.XPATH, f'//button[@value={station_index}]'


    @staticmethod
    def choose_rent_duration(duration):
        return By.XPATH, f'//div[@class="Dropdown-option" and contains(text(), {duration})]'

    @staticmethod
    def choose_colour(colour):
        return By.ID, f"{colour}"
