from selenium.webdriver.common.by import By
class PersonalAccountLocators:
    # Поле ввода email
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/../input")
    # Поле ввода пароля
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@type='password']")
    # Кнопка Войти
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")
    # Кнопка Оформить заказ
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Кнопка История заказов
    HISTORY_ORDER_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    # Кнопка Выход
    LOGOUT_BUTTON = By.XPATH, "//button[text()='Выход']"