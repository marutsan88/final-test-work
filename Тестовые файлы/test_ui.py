import allure
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url_ui = config.get("base_url_ui")


@allure.feature("UI тесты для функционала корзины.")
@allure.title("Тест на поиск товара и добавление его в корзину.")
@allure.description(
    "Выполняем поиск товара согласно полученным данным, проверяем, что товар был добавлен в корзину."
)
@allure.id(1)
@allure.severity("Blocker")
def test_search_product(main_page, cart_page):
    product_name = "Гриб Рейши, 60 капсул по 500 мг"
    main_page.search_product_by_search_field(product_name)
    product_name_added_to_cart = main_page.add_product_to_cart(product_name)
    with allure.step(
        "Проверяем, что переданное название товара совпадает с названием товара, который мы добавили в корзину."
    ):
        assert product_name_added_to_cart == product_name
    main_page.go_to_cart()
    result_to_add = cart_page.find_product_in_cart(product_name)
    with allure.step("Проверяем, что товар действительно находится в корзине."):
        assert result_to_add is True


@allure.feature("UI тесты для функционала корзины.")
@allure.title("Тест на удаление товара из корзины.")
@allure.description(
    "Выполняем поиск товара согласно полученным данным, переходим в корзину, удаляем товар, проверяем, что товар был удален."
)
@allure.id(2)
@allure.severity("Blocker")
def test_delete_product_from_cart(main_page, cart_page):
    product_name = "Гриб Рейши, 60 капсул по 500 мг"
    main_page.search_product_by_search_field(product_name)
    product_name_added_to_cart = main_page.add_product_to_cart(product_name)
    with allure.step(
        "Проверяем, что переданное название товара совпадает с названием товара, который мы добавили в корзину."
    ):
        assert product_name_added_to_cart == product_name
    main_page.go_to_cart()
    result_to_delete = cart_page.delete_product_in_cart(product_name)
    with allure.step("Проверяем, что товар действительно отсутствует в корзине."):
        assert result_to_delete is True


@allure.feature("UI тесты для функционала корзины.")
@allure.title("Тест на изменение количества товара в корзине.")
@allure.description(
    "Выполняем поиск товара согласно полученным данным, переходим в корзину, изменяем количество товара, проверяем, что количество изменилось."
)
@allure.id(3)
@allure.severity("Blocker")
def test_change_amount(main_page, cart_page):
    product_name = "Гриб Рейши, 60 капсул по 500 мг"
    main_page.search_product_by_search_field(product_name)
    product_name_added_to_cart = main_page.add_product_to_cart(product_name)
    with allure.step(
        "Проверяем, что переданное название товара совпадает с названием товара, который мы добавили в корзину."
    ):
        assert product_name_added_to_cart == product_name
    main_page.go_to_cart()
    amount_before_change = cart_page.control_amount_product_in_cart(product_name)
    amount_to_change = 3
    with allure.step("Проверяем, что количество товара до изменений, равно 1."):
        cart_page.change_amount_product_in_cart(product_name, "more", amount_to_change)
    amount_after_change = cart_page.control_amount_product_in_cart(product_name)
    with allure.step(
        "Проверяем, что количество товара изменилось на необходимое значение."
    ):
        assert int(amount_before_change) + amount_to_change == int(amount_after_change)
