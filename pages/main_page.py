import allure
from pages.base_page import BasePage
from locators.main_locators import MainLocators as main_locators
class MainPage(BasePage):
    @allure.step("Клик по кнопке Конструктор")
    def click_on_constructor(self):
        self.wait_element_visibility(main_locators.CONSTRUCTOR_BUTTON)
        self.click_element(main_locators.CONSTRUCTOR_BUTTON)
        return self.find_element(main_locators.CONSTRUCTOR_INSCRIPTION)

    @allure.step("Клик по кнопке Лента заказов")
    def click_on_order_feed_button(self):
        self.wait_element_visibility(main_locators.ORDER_FEED_BUTTON)
        self.click_element(main_locators.ORDER_FEED_BUTTON)
        return self.get_current_url()

    @allure.step("Клик по ингрeдиенту")
    def click_on_ingredient(self):
        self.click_element(main_locators.FLUORESCENT_BUN)
        self.wait_element_visibility(main_locators.INGREDIENT_WINDOW)
        return self.find_element(main_locators.INGREDIENT_WINDOW)

    @allure.step("Клик по кнопке закрытия всплывающего окна")
    def click_on_close_window(self):
        self.click_element(main_locators.CLOSE_BUTTON)
        self.wait_not_visibility_element(main_locators.INGREDIENT_WINDOW)
        return self.find_element(main_locators.CLOSE_BUTTON)

    @allure.step("Добавление ингредиента в заказ")
    def add_ingredient_in_order(self):
        self.wait_element_visibility(main_locators.COUNTER_BUN)
        counter = self.get_text(main_locators.COUNTER_BUN)
        self.drag_and_drop(main_locators.FLUORESCENT_BUN, main_locators.ADDITION_AREA_INGREDIENT)
        new_counter = self.get_text(main_locators.COUNTER_BUN)
        return counter, new_counter

    @allure.step("Клик по кнопке Оформить заказ")
    def click_create_order_button(self):
        self.wait_element_visibility(main_locators.CREATE_ORDER_BUTTON)
        self.click_element(main_locators.CREATE_ORDER_BUTTON)
        self.wait_element_visibility(main_locators.CREATE_ORDER_BUTTON)
        return self.find_element(main_locators.CREATE_ORDER_BUTTON)
