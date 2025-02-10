import pytest
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv()


@pytest.fixture
def driver():
    """
    Запускает инициализацию драйвера
    """
    service = Service(executable_path=ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument("--window-size=1920,1080")
    # options.add_argument("--start-maximized")
    # options.add_argument("--incognito")
    # options.add_argument("--disable-cache")
    # options.add_argument("--ignore-certificate-errors")
    driver = webdriver.Chrome(service=service, options=options)
    # driver.set_window_size(1920, 1080)
    # driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    """
    Фикстура для ожидания.
    """
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1)
    return wait
