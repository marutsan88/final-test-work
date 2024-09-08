from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def find_element_and_click(self, css_selector: str):
        """
        Данный метод находит элемент на странице по его
        селектору и нажимает на элемент.
        Args:
            css_selector (str): css_selector элемента.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()

    @allure.step(
        "Выполняем поиск товара в поисковой строке по переданному наименованию - '{product_name}'."
    )
    def search_product_by_search_field(self, product_name: str):
        """
        Метод для поиска товара через поисковую строку.
        Args:
            product_name (str): наименование продукта для поиска.
        """
        search_field = self._driver.find_element(
            By.XPATH, "//input[@placeholder='Поиск товаров']"
        )
        search_field.send_keys(product_name)
        self.find_element_and_click("div.searchpro__field-button-container")

    @allure.step(
        "Находим на странице результатов поиска необходимый нам товар - '{product_name_to_add}' и добавляем его в корзину."
    )
    def add_product_to_cart(self, product_name_to_add: str) -> str:
        """
        Метод для добавления товара в корзину согласно переданному наименованию.
        Args:
            product_name_to_add (str): наименование продукта который необходимо добавить в корзину.
        Returns:
            str: наименование товара, который был добавлен в корзину.
        """
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.rating_search_product")
            )
        )
        product_info_containers = self._driver.find_elements(
            By.CSS_SELECTOR, "div.product__item"
        )
        for container in product_info_containers:
            product_img = container.find_element(By.CSS_SELECTOR, "img")
            product_name = product_img.get_attribute("alt")
            if product_name == product_name_to_add:
                add_button = container.find_element(
                    By.CSS_SELECTOR, "div.product__buy button"
                )
                add_button.click()
                return product_name

    @allure.step("Переходим на страницу корзины.")
    def go_to_cart(self):
        """
        Метод позволяет перейти в корзину.
        """
        self.find_element_and_click("a[href='/cart/']")
        self.find_element_and_click("a.dropdown-go-over")
