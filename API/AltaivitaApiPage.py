import os
import requests
from typing import Dict, Any, Tuple
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

with open("config.json", "r") as config_file:
    config = json.load(config_file)

api_data = config.get("api")
base_url_api = config.get("base_url_api")

class AltaivitaApi:
    def __init__(self, url):
        self.url = url
        self.login = os.getenv("LOGIN")
        self.password = os.getenv("PASSWORD")

    def login_to_site(self) -> Tuple[Dict[str, Any], int]:
        """Метод для выполнения входа на сайт."""
        login_data = {
            'login': self.login,
            'password': self.password
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(
            f"{self.url}login.php", 
            data=login_data, 
            headers=headers
        )
        return response.json(), response.status_code

    def add_product_to_cart_from_preview(self, quantity: str) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет добавить товар в корзину."""
        api_data_new = api_data.copy()
        api_data_new["quantity"] = quantity
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        result_add_to_cart = requests.post(
            self.url + "add_products_to_cart_from_preview.php",
            data=api_data_new,
            headers=headers,
        )
        return result_add_to_cart.json(), result_add_to_cart.status_code

    def delete_product_from_cart(self) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет удалить категорию товара из корзины."""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        result_delete_from_cart = requests.post(
            self.url + "delete_products_from_cart_preview.php",
            data=api_data,
            headers=headers,
        )
        return result_delete_from_cart.json(), result_delete_from_cart.status_code

    def change_amount_product_from_preview(self) -> Tuple[Dict[str, Any], int]:
        """Метод позволяет изменить количество товара из превью товара."""
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        result_change_from_preview = requests.post(
            self.url + "delete_products_from_cart_preview_by_productID.php",
            data=api_data,
            headers=headers,
        )
        return result_change_from_preview.json(), result_change_from_preview.status_code
