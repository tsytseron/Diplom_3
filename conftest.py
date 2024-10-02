import pytest
import requests
from selenium import webdriver
from data_generators import generate_user_data
from data import Data


def _get_driver(name):
    if name == 'chrome':
        return webdriver.Chrome()
    elif name == 'firefox':
        return webdriver.Firefox()
    else:
        raise TypeError('Driver is not found')


@pytest.fixture(scope="function", params=["chrome", "firefox"])
def driver(request):
    driver = _get_driver(request.param)
    driver.get(Data.BURGER_SITE)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def create_user():
    user_data = generate_user_data()
    resp = requests.post(Data.CREATE_USER, data=user_data)
    token = resp.json().get("accessToken")
    yield user_data, resp
    requests.delete(Data.DELETE_DATA, headers={"Authorization": f'{token}'})