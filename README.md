Diplpm_3 UI автотесты с отчётами для сайта https://stellarburgers.nomoreparties.site/

allure_results: отчёты о тестировании

conftest.py:  
Фикстура для Chrome и Firefox, создаёт и удаляет пользователя, генерирует логин, пароль и имя пользователя

data.py:  
Сайт  
Ручки из документации к сайту  
Ингредиенты

data_generators.py:  
Вспомогательные методы для генерирования данных

locators:  
main_locators.py - локаторы элементов главной страницы  
order_feed_locators.py - локаторы элементов страницы заказов  
password_locators.py - локаторы элементов восстановления пароля  
personal_account_locators.py - локаторы элементов личного кабинета

pages:
base_page.py - базовые методы  
main_page.py - методы главной страницы  
order_feed_page.py - методы страницы заказа  
personal_account_page.py - методы личного кабинета

tests:
test_main_page.py - тестирование методов главной страницы  
test_order_feed_page.py - тестирование методов страницы заказов  
test_password_page.py - тестирование методов восстановления пароля  
test_personal_account_page.py - тестирование методов личного кабинета
