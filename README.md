# final-test-work
sky pro

SQL 
1. Вывести все уникальные названия продуктов 

   SELECT DISTINCT product_name FROM Products;
   
Этот запрос выбирает все уникальные названия продуктов из таблицы Products, исключая дубликаты.

2. Вывести название продукта с самым высоким содержанием белка (protein) 
   SELECT product_name
   FROM Products join NutritionalInformation on Products.product_id = NutritionalInformation.product_id
   ORDER BY protein DESC LIMIT 1;
   
Этот запрос соединяет таблицы Products и NutritionalInformation по полю product_id, выбирает название продукта (product_name) и сортирует результаты по убыванию содержания белка (protein). Затем он ограничивает вывод одной строкой с помощью оператора LIMIT 1.

3.Выведите id, название и стоимость продуктов с содержанием клетчатки (fiber) более 5 граммов 
  SELECT p.product_id, p.product_name, p.price
   FROM Products AS p JOIN NutritionalInformation AS ni ON p.product_id = ni.product_id
   WHERE ni.fiber > 5;
   
Этот запрос соединяет таблицы Products и NutritionalInformation по полю product_id, выбирает product_id, product_name и price из таблицы Products, и фильтрует результаты по тем продуктам, у которых содержание клетчатки (ni.fiber) превышает 5 граммов.

4.Подсчитать общую сумму калорий для продуктов каждой категории, не учитывая продукты с нулевым жиром 
  SELECT c.category_id, SUM(p.calories)
   FROM Products AS p
   JOIN Categories AS c ON p.category_id = c.category_id
   JOIN NutritionalInformation AS ni ON p.product_id = ni.product_id
   WHERE ni.fat > 0
   GROUP BY c.category_id;
   
Этот запрос соединяет таблицы Products, Categories и NutritionalInformation, выбирает category_id и суммирует калории (SUM(p.calories)) для каждой категории. Он также фильтрует результаты, чтобы исключить продукты с нулевым содержанием жира (WHERE ni.fat > 0).

5. Рассчитать среднюю цену товаров каждой категории 
   SELECT c.category_name, AVG(p.price) AS average_price
   FROM Products AS p
   JOIN Categories AS c ON p.category_id = c.category_id
   GROUP BY c.category_id;
   
Этот запрос соединяет таблицы Products и Categories, выбирает category_name и рассчитывает среднюю цену товаров (AVG(p.price)) для каждой категории.









