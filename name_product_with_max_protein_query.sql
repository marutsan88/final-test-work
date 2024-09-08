SELECT product_name
   FROM Products
   ORDER BY (SELECT MAX(protein) FROM NutritionalInformation WHERE product_id = Products.product_id) DESC
   LIMIT 1;