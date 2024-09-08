SELECT c.category_id, SUM(p.calories)
   FROM Products AS p
   JOIN Categories AS c ON p.category_id = c.category_id
   JOIN NutritionalInformation AS ni ON p.product_id = ni.product_id
   WHERE ni.fat > 0
   GROUP BY c.category_id;