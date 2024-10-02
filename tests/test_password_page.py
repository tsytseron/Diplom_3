import allure
from pages.password_page import PasswordPage
class TestPasswordPage:
    @allure.title("Переход на страницу восстановления пароля по кнопке Восстановить пароль")
    @allure.description("Проверка возможности перехода по кнопке Восстановить пароль")
    def test_click_on_btn_recovery_page(self, driver):
        password_restore = PasswordPage(driver)
        password_restore.go_to_personal_account()
        assert password_restore.click_and_wait_restore_button()

    @allure.title("Ввод email и клик по кнопке Восстановить")
    @allure.description("Проверка возможности восстановления пароля по email")
    def test_input_email_and_click_on_restore_button(self, driver):
        password_restore = PasswordPage(driver)
        password_restore.go_to_personal_account()
        password_restore.click_and_wait_restore_button()
        assert password_restore.input_email_and_click_restore_button()

    @allure.title("Клик по кнопке показать/скрыть пароль делая поле активным")
    @allure.description("Проверка видимости ввода пароля после клика по глазу")
    def test_click_password_visible_button(self, driver):
        password_restore = PasswordPage(driver)
        password_restore.go_to_personal_account()
        password_restore.click_and_wait_restore_button()
        password_restore.input_email_and_click_restore_button()
        password_restore.input_password()
        assert password_restore.click_on_eye_button()