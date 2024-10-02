import allure
from data_generators import generate_user_data
from pages.base_page import BasePage
from locators.password_locators import PasswordLocators as password
class PasswordPage(BasePage):
    @allure.title("Переход в личный кабинет")
    def go_to_personal_account(self):
        self.wait_element_visibility(password.PERSONAL_ACCOUNT_INSCRIPTION)
        self.click_element(password.PERSONAL_ACCOUNT_INSCRIPTION)

    @allure.title("Переход по кнопке Восстановить пароль")
    def click_and_wait_restore_button(self):
        self.wait_element_visibility(password.RESTORE_PASSWORD_HYPERLINK)
        self.click_element(password.RESTORE_PASSWORD_HYPERLINK)
        return self.find_element(password.RESTORE_PASSWORD_INSCRIPTION)

    @allure.title("Ввод email в поле ввода и клик по кнопке восстановления пароля")
    def input_email_and_click_restore_button(self):
        self.wait_element_visibility(password.EMAIL_INPUT_FIELD)
        self.click_element(password.EMAIL_INPUT_FIELD)
        user_data = generate_user_data()
        self.enter_text(password.EMAIL_INPUT_FIELD, user_data['email'])
        self.click_element(password.RESTORE_BUTTON)
        self.wait_element_visibility(password.PASSWORD_INPUT_FIELD)
        return self.find_element(password.PASSWORD_INPUT_FIELD)

    @allure.title("Ввод рандомного пароля в поле Пароль")
    def input_password(self):
        self.wait_element_visibility(password.PASSWORD_INPUT_FIELD)
        user_data = generate_user_data()
        self.enter_text(password.PASSWORD_INPUT_FIELD, user_data['password'])

    @allure.step("Клик на глаз рядом с вводом пароля")
    def click_on_eye_button(self):
        self.click_element(password.EYE_BUTTON)
        return self.find_element(password.VISIBLE_PASSWORD_INPUT)
