import allure
from data import Data
from pages.password_page import PasswordPage
from pages.personal_account_page import PersonalAccountPage
class TestPersonalAccountPage:
    @allure.title("Переход по клику на Личный кабинет")
    @allure.description("Проверка работы кнопки личного кабинета")
    def test_click_goto_personal_account(self, driver):
        password_recovery = PasswordPage(driver)
        password_recovery.go_to_personal_account()
        assert password_recovery.get_current_url() == Data.LOGIN_PAGE

    @allure.title("Переход в раздел История заказов")
    @allure.description("Проверка открытия страницы истории заказов у авторизованного пользователя")
    def test_click_goto_history_orders(self, driver, create_user):
        password_recovery = PasswordPage(driver)
        personal_area = PersonalAccountPage(driver)
        password_recovery.go_to_personal_account()
        personal_area.authorization(create_user)
        password_recovery.go_to_personal_account()
        personal_area.open_history_orders()
        assert personal_area.get_current_url() == Data.HISTORY_PAGE

    @allure.title("Выход из аккаунта")
    @allure.description("Проверка выхода из аккаунта")
    def test_logout(self, driver, create_user):
        password_recovery = PasswordPage(driver)
        personal_area = PersonalAccountPage(driver)
        password_recovery.go_to_personal_account()
        personal_area.authorization(create_user)
        password_recovery.go_to_personal_account()
        personal_area.logout()
        assert personal_area.get_current_url() == Data.LOGIN_PAGE
