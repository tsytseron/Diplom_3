import allure
from data import Data
from pages.main_page import MainPage
from pages.password_page import PasswordPage
from pages.personal_account_page import PersonalAccountPage
class TestMainPage:
    @allure.title("Переход по клику на кнопку Конструктор")
    @allure.description("Проверка перехода по кнопке Конструктор")
    def test_click_button_construct(self, driver):
        main = MainPage(driver)
        password_restore = PasswordPage(driver)
        password_restore.go_to_personal_account()
        assert main.click_on_constructor()

    @allure.title("Переход по клику на кнопку Лента заказов")
    @allure.description("Проверка перехода на страницу ленты заказов")
    def test_click_button_list_order(self, driver):
        main = MainPage(driver)
        main.click_on_order_feed_button()
        assert main.get_current_url() == Data.FEED_PAGE

    @allure.title("Открытие модального окна при клике на ингредиент")
    @allure.description("Проверка появления всплывающего окна с деталями при клике на ингредиент")
    def test_click_on_ingredient(self, driver):
        main = MainPage(driver)
        assert main.click_on_ingredient()

    @allure.title("Закрытие модального окна ингредиента")
    @allure.description("Проверка закрытия всплывающего окна кликом на крестик")
    def test_click_close_btn_modal(self, driver):
        main = MainPage(driver)
        main.click_on_ingredient()
        assert main.click_on_close_window()

    @allure.title("Добавление ингредиента в заказ")
    @allure.description("Проверка увеличения счётчика колличества при добавлении ингредиента в заказ")
    def test_check_counter_ingredients(self, driver):
        main = MainPage(driver)
        counter = main.add_ingredient_in_order()
        assert int(counter[0]) == 0 and int(counter[1]) == 2

    @allure.title("Оформление заказа авторизованным пользователем")
    @allure.description("Проверка возможности оформить заказ авторизованным пользователем")
    def test_create_order_authorized_user(self, driver, create_user):
        main = MainPage(driver)
        personal_account = PersonalAccountPage(driver)
        password_restore = PasswordPage(driver)
        password_restore.go_to_personal_account()
        personal_account.authorization(create_user)
        main.add_ingredient_in_order()
        assert main.click_create_order_button()
