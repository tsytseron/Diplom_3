import allure
from seletools.actions import drag_and_drop
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск {locator}')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидание появления {locator}')
    def wait_element_visibility(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание исчезновения {locator}')
    def wait_not_visibility_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step('Клик по {locator}')
    def click_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Скроллинг к {locator}')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Печать {text} в {locator}')
    def enter_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получение текста из {locator}')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Ожидание URL текущей страницы')
    def wait_url_contains(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))
        return self.driver.current_url

    @allure.step('Получение URL страницы на которой находимся')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Поиск всех элементов {locator}')
    def find_all_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Перемещение элемента с {point_from} на {point_where}')
    def drag_and_drop(self, point_from, point_where):
        source_element = self.find_element(point_from)
        target_element = self.find_element(point_where)
        drag_and_drop(self.driver, source_element, target_element)
