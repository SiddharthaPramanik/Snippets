CREATE SCHEMA practice;
USE practice;
DROP TABLE IF EXISTS sales;
CREATE TABLE sales (
  sales_month INTEGER,
  product VARCHAR(4),
  amount INTEGER
);
INSERT INTO sales
  (sales_month, product, amount)
VALUES
	(1, 'A', 100),
	(1, 'B', 150),
	(2, 'A', 250),
	(2, 'B', 175),
	(3, 'A', 180),
	(3, 'B', 300),
	(4, 'A', 390),
	(4, 'B', 200),
	(5, 'A', 400),
	(5, 'B', 278),
	(6, 'A', 285),
	(6, 'B', 350),
	(7, 'A', 100),
	(7, 'B', 150),
	(8, 'A', 250),
	(8, 'B', 175),
	(9, 'A', 180),
	(9, 'B', 300),
	(10, 'A', 390),
	(10, 'B', 200),
	(11, 'A', 400),
	(11, 'B', 278),
	(12, 'A', 285),
	(12, 'B', 350);
    
SELECT * FROM sales;
SELECT sales_month , product, 
	(amount / (LAG(amount, 1) OVER (PARTITION BY product)) - 1 )* 100 as MoM
FROM sales;