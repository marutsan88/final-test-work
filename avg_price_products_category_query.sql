SELECT c.category_name, AVG(p.price) AS average_price
   FROM Products AS p
   JOIN Categories AS c ON p.category_id = c.category_id
   GROUP BY c.category_id;