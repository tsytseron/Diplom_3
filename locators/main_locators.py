from selenium.webdriver.common.by import By
class MainLocators:
    # Кнопка Конструктор
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Надпись Соберите бургер
    CONSTRUCTOR_INSCRIPTION = (By.CSS_SELECTOR, "h1.text.text_type_main-large.mb-5.mt-10")
    # Кнопка Лента заказов
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    # Надпись Лента заказов
    ORDER_FEED_INSCRIPTION = (By.XPATH, "//h1[text()='Лента заказов']")
    # Карточка флюоресцентной булки
    FLUORESCENT_BUN = (By.XPATH, "//p[text()='Флюоресцентная булка R2-D3']")
    # Всплывающее окно с деталями ингредиента
    INGREDIENT_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']")
    # Кнопка закрытия всплывающего окна
    CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'close')]")
    # Область добавления ингредиентов
    ADDITION_AREA_INGREDIENT = (By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket__29Cd7')]")
    # Контейнер ингредиента
    COUNTER_BUN = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")
    # Кнопка Оформить заказ
    CREATE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    # Всплывающее окно подтверждения заказа
    CREATE_ORDER_WINDOW = (By.CLASS_NAME, "Modal_modal__container__Wo2l_")
