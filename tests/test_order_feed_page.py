import allure
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.password_page import PasswordPage
from pages.personal_account_page import PersonalAccountPage
class TestOrderFeedPage:
    @allure.title("Отображение деталей заказа при клике на него")
    @allure.description("Проверка открытия всплывающего окна с деталями при клике на заказ")
    def test_click_on_order(self, driver):
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        main.click_on_order_feed_button()
        assert order_feed.click_on_order()

    @allure.title("Отображение заказов пользователя в История заказов")
    @allure.description("Проверка отображения заказов пользователя из раздела История заказов на странице Лента заказов")
    def test_user_order_in_list_order(self, driver, create_user):
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        password_restore = PasswordPage(driver)
        password_restore.go_to_personal_account()
        number = personal_account.auth_and_change_order(create_user)
        number = '#0' + number[-1]
        main.click_on_order_feed_button()
        order_texts = order_feed.all_order_inscription()
        assert number in order_texts

    @allure.title("Проверка счетчика заказа за все время")
    @allure.description("Проверка работы счетчика выполненных заказов за все время заказов")
    def test_checking_orders_counter_all_time(self, driver, create_user):
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        password_restore = PasswordPage(driver)
        main.click_on_order_feed_button()
        counter_orders = order_feed.number_orders_all_time()
        password_restore.go_to_personal_account()
        personal_account.auth_and_change_order(create_user)
        main.click_on_order_feed_button()
        new_counter_orders = order_feed.number_orders_all_time()
        assert int(new_counter_orders) > int(counter_orders)

    @allure.title("Проверка счетчика заказа за сегодня")
    @allure.description("Проверка работы счетчика выполненных заказов за сегодня")
    def test_checking_order_counter_today(self, driver, create_user):
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        password_restore = PasswordPage(driver)
        main.click_on_order_feed_button()
        counter_orders = order_feed.number_orders_today()
        password_restore.go_to_personal_account()
        personal_account.auth_and_change_order(create_user)
        main.click_on_order_feed_button()
        new_counter_orders = order_feed.number_orders_today()
        assert int(new_counter_orders) > int(counter_orders)

    @allure.title("Появление оформленного заказа в разделе В работе")
    @allure.description("Проверка появления номера заказа в разделе готовящихся заказов В работе после оформления заказа")
    def test_check_create_order_progress_section(self, driver, create_user):
        main = MainPage(driver)
        order_feed = OrderFeedPage(driver)
        personal_account = PersonalAccountPage(driver)
        password_restore = PasswordPage(driver)
        password_restore.go_to_personal_account()
        number = personal_account.auth_and_change_order(create_user)
        number = '0' + number[-1]
        main.click_on_order_feed_button()
        order_feed.all_order_inscription()
        order_number = order_feed.check_order_progress_field()
        assert number in order_number
