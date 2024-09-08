SELECT p.product_id, p.product_name, p.price
   FROM Products AS p JOIN NutritionalInformation AS ni ON p.product_id = ni.product_id
   WHERE ni.fiber > 5;