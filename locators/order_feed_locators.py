from selenium.webdriver.common.by import By
class OrderFeedLocators:
    # Первый заказ
    FIRST_ORDER = (By.XPATH, "//div/ul/li[1]")
    # Все заказы
    ALL_ORDERS = (By.XPATH, "//*[contains(@class, 'text text_type_digits-default')]")
    # Счетчик Выполнено за все время
    ORDER_ALL_COUNTER = (By.XPATH, "//div/div[2]/p[2]")
    # Счетчик Выполнено за сегодня
    ORDER_TODAY_COUNTER = (By.XPATH, "//p[contains(@class, 'text_type_main') and contains(text(), 'Выполнено за сегодня')]/following-sibling::p[contains(@class, 'text_type_digits-large')]")
    # Поле готовящихся заказов
    ORDERS_PROGRESS_FIELD = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(@class, 'text_type_digits-default')]")
    # Надпись поля готовящихся заказов
    ORDERS_PROGRESS_INSCRIPTION = (By.XPATH, "//*[text() = 'Все текущие заказы готовы!']")
    # Всплывающее окно заказа
    CONTAINER_ORDER_WINDOW = (By.XPATH, ".//div[contains(@class, 'Modal_orderBox__1xWdi')]")