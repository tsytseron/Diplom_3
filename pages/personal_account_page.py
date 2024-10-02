import allure
from data_generators import created_orders
from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators as personal
class PersonalAccountPage(BasePage):

    @allure.step("Авторизация")
    def authorization(self, create_user):
        user_date, resp = create_user
        self.enter_text(personal.EMAIL_INPUT_FIELD, user_date['email'])
        self.enter_text(personal.PASSWORD_INPUT_FIELD, user_date['password'])
        self.click_element(personal.LOGIN_BUTTON)
        self.wait_element_visibility(personal.CREATE_ORDER_BUTTON)
        return user_date['email'], user_date['password']

    @allure.step("Авторизация и оформление заказа")
    def auth_and_change_order(self, create_user):
        user_date, resp = create_user
        email, password = self.authorization(create_user)
        number = created_orders(resp)
        number = str(number.json()['order']['number'])
        return email, password, number

    @allure.title("Переход по истории заказов")
    def open_history_orders(self):
        self.wait_element_visibility(personal.HISTORY_ORDER_BUTTON)
        self.click_element(personal.HISTORY_ORDER_BUTTON)
        self.wait_element_visibility(personal.HISTORY_ORDER_BUTTON)

    @allure.step("Выход из аккаунта")
    def logout(self):
        self.wait_element_visibility(personal.LOGOUT_BUTTON)
        self.click_element(personal.LOGOUT_BUTTON)
        self.wait_element_visibility(personal.LOGIN_BUTTON)
