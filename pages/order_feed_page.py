import allure
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators as order_locators
class OrderFeedPage(BasePage):
    @allure.step("Клик на заказ")
    def click_on_order(self):
        self.wait_element_visibility(order_locators.FIRST_ORDER)
        self.find_element(order_locators.FIRST_ORDER).click()
        self.wait_element_visibility(order_locators.CONTAINER_ORDER_WINDOW)
        return self.find_element(order_locators.CONTAINER_ORDER_WINDOW)

    @allure.step("Поиск надписи Все заказы")
    def all_order_inscription(self):
        self.wait_element_visibility(order_locators.ALL_ORDERS)
        return self.return_locators_list(order_locators.ALL_ORDERS)

    @allure.step("Число выполненных заказов за все время")
    def number_orders_all_time(self):
        self.wait_element_visibility(order_locators.ORDER_ALL_COUNTER)
        return self.get_text(order_locators.ORDER_ALL_COUNTER)

    @allure.step("Число выполненных заказов за сегодня")
    def number_orders_today(self):
        self.wait_element_visibility(order_locators.ORDER_TODAY_COUNTER)
        return self.get_text(order_locators.ORDER_TODAY_COUNTER)

    @allure.step("Проверка поля с готовящимися заказами")
    def check_order_progress_field(self):
        self.wait_element_visibility(order_locators.ORDERS_PROGRESS_FIELD)
        return self.return_locators_list(order_locators.ORDERS_PROGRESS_FIELD)

    @allure.step("Создание списка всех готовящихся заказов")
    def return_locators_list(self, locator):
        all_locators = self.find_all_element(locator)
        locator_text = []
        for order in all_locators:
            locator_text.append(order.text)
        return locator_text
