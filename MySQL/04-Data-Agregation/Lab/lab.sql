USE `restaurant`;
# Problem 1 Departments Info
SELECT e.department_id, COUNT(department_id) as `Number of employees` FROM employees as e
GROUP BY department_id;


# Problem 2 Average Salary
SELECT department_id, ROUND(AVG(salary), 2) as `Average Salary` FROM employees
GROUP BY department_id
ORDER BY department_id;


# Problem 3 Minimum Salary
SELECT department_id, ROUND(MIN(salary), 2) as min_salary FROM employees
GROUP BY department_id
HAVING min_salary > 800
ORDER BY department_id;


# Problem 4 Appetizers Count
SELECT COUNT(price) as apetizers_count FROM products
WHERE category_id = 2 and price > 8;


# Problem 5 Menu Prices
SELECT category_id,
       ROUND(AVG(price), 2) AS average_price,
       ROUND(MIN(price), 2) AS cheapest_product,
       ROUND(MAX(price), 2) AS most_expensive_product
FROM products
GROUP BY category_id
ORDER BY category_id;