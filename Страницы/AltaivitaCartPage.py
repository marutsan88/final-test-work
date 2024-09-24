from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:

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

    @allure.step("Проверяем находится ли в корзине товар, который ранее мы добавили.")
    def find_product_in_cart(self, product_name_to_find: str) -> bool:
        """
        Данный метод находит находит товар в корзине и возвращает True или False.
        Args:
            product_name_to_find (str): наименование товара, который необходимо найти в корзине.
        Returns:
            bool: товар найден или не найден.
        """
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.basket__name"))
        )
        products = self._driver.find_elements(By.CSS_SELECTOR, "a.basket__name")
        for product in products:
            if product.text.strip() == product_name_to_find:
                return True
        return False

    @allure.step("Удаляем необходимый товар из корзины.")
    def delete_product_in_cart(self, product_name_to_delete: str) -> bool:
        """
        Данный метод позволяет удалить товар из корзины и возвращает True или False.
        Args:
            product_name_to_delete (str): наименование товара, который необходимо удалить.
        Returns:
            bool: товар удален или нет.
        """
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, "div.basket__delete i")
            )
        )
        delete_buttons = self._driver.find_elements(
            By.CSS_SELECTOR, "div.basket__delete i"
        )
        products = self._driver.find_elements(By.CSS_SELECTOR, "a.basket__name")
        for i in range(len(products)):
            if products[i].text.strip() == product_name_to_delete:
                delete_buttons[i].click()
                return True
        return False

    @allure.step("Изменяем количество товаров в корзине.")
    def change_amount_product_in_cart(
        self, product_name_to_change: str, type_button: str, amount: int
    ):
        """
        Данный метод позволяет удалить товар из корзины и возвращает True или False.
        Args:
            product_name_to_change (str): наименование товара, количество которого необходимо изменить.
            type_button (str): less или more, уменьшить количество или увеличить.
            amount (int): количество, на которое необходимо уменьшить/увеличить.
        """
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.basket__name"))
        )
        products = self._driver.find_elements(By.CSS_SELECTOR, "a.basket__name")
        less_buttons = self._driver.find_elements(By.CSS_SELECTOR, "button.less")
        more_buttons = self._driver.find_elements(By.CSS_SELECTOR, "button.more")
        result_less = (
            int(self.control_amount_product_in_cart(product_name_to_change)) - amount
        )
        result_more = (
            int(self.control_amount_product_in_cart(product_name_to_change)) + amount
        )
        for i in range(len(products)):
            if products[i].text.strip() == product_name_to_change:
                if type_button == "less":
                    for _ in range(amount + 1):
                        res = self.control_amount_product_in_cart(
                            product_name_to_change
                        )
                        if int(res) > result_less:
                            less_buttons[i].click()
                elif type_button == "more":
                    for _ in range(amount + 1):
                        res_n = self.control_amount_product_in_cart(
                            product_name_to_change
                        )
                        if int(res_n) < result_more:
                            more_buttons[i].click()

    @allure.step("Проверяем количество товара.")
    def control_amount_product_in_cart(
        self, product_name_to_control_amount: str
    ) -> str:
        """
        Данный метод проверяет какое количество данного товара находится в корзине.
        Args:
            product_name_to_control_amount (str): наименование товара, количество которого необходимо узнать.
        Returns:
            str: количество товара.
        """
        products = self._driver.find_elements(By.CSS_SELECTOR, "a.basket__name")
        amount_products = self._driver.find_elements(By.CSS_SELECTOR, "span.num")
        for i in range(len(products)):
            if products[i].text.strip() == product_name_to_control_amount:
                WebDriverWait(self._driver, 10).until(
                    EC.visibility_of(amount_products[i])
                )
                return amount_products[i].text
