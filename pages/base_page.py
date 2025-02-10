from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def element_is_visible(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.visibility_of_element_located(locator))

    def element_is_clickable(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.element_to_be_clickable(locator))

    def element_is_present(self, locator, timeout=10):
        return wait(self.driver, timeout=timeout).until(EC.presence_of_element_located(locator))

    def alert_is_visible(self, timeout=10):
        wait(self.driver, timeout=timeout).until(EC.alert_is_present())

    def double_click(self, element):
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def right_click(self, element):
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def action_move_to_element(self, element):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def action_drag_and_drop(self, source_element, target_elem):
        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_elem)
        action.perform()
