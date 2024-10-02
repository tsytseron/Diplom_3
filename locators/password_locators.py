from selenium.webdriver.common.by import By
class PasswordLocators:
    # Надпись кнопки Личный Кабинет
    PERSONAL_ACCOUNT_INSCRIPTION = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']/p[text() ='Личный Кабинет']")
    # Гиперссылка Восстановить пароль
    RESTORE_PASSWORD_HYPERLINK = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Восстановить пароль']")
    # Надпись Восстановления пароля
    RESTORE_PASSWORD_INSCRIPTION = (By.XPATH, "//h2[text()='Восстановление пароля']")
    # Кнопка "Восстановить"
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    # Поле ввода пароля
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@type='password']")
    # Поле ввода email
    EMAIL_INPUT_FIELD = (By.XPATH, "//label[text()='Email']/../input")
    # Иконка глаза рядом с полем ввода пароля
    EYE_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon') and contains(@class, 'input__icon-action')]")
    # Видимый ввод пароля
    VISIBLE_PASSWORD_INPUT = (By.XPATH, "//div[contains(@class, 'input_status_active')]")