USE `soft_uni`;
# Problem 1 Find Names of All Employees by First Name
SELECT e.first_name, e.last_name
FROM employees as e
WHERE LOWER(e.first_name) LIKE 'sa%';


# Problem 2 Find Names of All Employees by Last Name
SELECT e.first_name, e.last_name
FROM employees as e
WHERE LOWER(e.last_name) LIKE '%ei%';


# Problem 3 Find First Names of All Employees
SELECT e.first_name
FROM employees AS e
WHERE e.department_id IN (3, 10)
  AND YEAR(e.hire_date) BETWEEN 1995 AND 2005
ORDER BY e.employee_id;

# Problem 4 Find All Employees Except Engineers
SELECT e.first_name, e.last_name
FROM employees AS e
WHERE e.job_title NOT LIKE '%engineer%'
ORDER BY e.employee_id;


# Problem 5 Find Towns with Name Length
SELECT t.name
FROM towns AS t
WHERE LENGTH(t.name) IN (5, 6)
ORDER BY t.name;


# Problem 6 Find Towns Starting With
SELECT t.town_id, t.name
FROM towns AS t
WHERE LOWER(LEFT(t.name, 1)) IN ('m', 'k', 'b', 'e')
ORDER BY t.name;


# Problem 7 Find Towns Not Starting With
SELECT t.town_id, t.name
FROM towns AS t
WHERE LOWER(LEFT(t.name, 1)) NOT IN ('r', 'b', 'd')
ORDER BY t.name;


# Problem 8 Create View Employees Hired After 2000 Year
CREATE VIEW v_employees_hired_after_2000 AS
SELECT e.first_name, e.last_name
FROM employees AS e
WHERE YEAR(e.hire_date) > 2000;


# Problem 9 Length Of Last Name
SELECT e.first_name, e.last_name
FROM employees AS e
WHERE e.last_name LIKE '_____';


USE `geography`;
# Problem 10 Countries Holding 'A' 3 or More Times
SELECT c.country_name, c.iso_code
FROM countries as c
WHERE LOWER(c.country_name) LIKE '%a%a%a%'
ORDER BY c.iso_code;


# Problem 11 Mix of Peak and River Names
SELECT p.peak_name, r.river_name,
CONCAT(LOWER(p.peak_name), LOWER(SUBSTR(r.river_name, 2))) AS mix
FROM peaks AS p, rivers AS r
WHERE LOWER(RIGHT(p.peak_name, 1)) = LOWER(LEFT(r.river_name, 1))
ORDER BY mix;


USE `diablo`;
# Problem 12 Games from 2011 and 2012 Year
SELECT g.name, DATE_FORMAT(g.start, '%Y-%m-%d') AS start
FROM games AS g
WHERE YEAR(g.start) IN (2011, 2012)
ORDER BY g.start, g.name
LIMIT 50;


# Problem 13 User Email Providers
SELECT u.user_name, SUBSTRING_INDEX(u.email, '@', -1) AS `Email Provider`
FROM users AS u
ORDER BY `Email Provider`, u.user_name;


# Problem 14 Get Users with IP Address Like Pattern
SELECT u.user_name, u.ip_address
FROM users AS u
WHERE u.ip_address LIKE '___.1%.%.___'
ORDER BY u.user_name;


# Problem 15 Show All Games with Duration and Part of the Day
SELECT g.name,
(
    CASE
        WHEN HOUR(g.start) BETWEEN 0 AND 11 THEN 'Morning'
        WHEN HOUR(g.start) BETWEEN 12 AND 17 THEN 'Afternoon'
        WHEN HOUR(g.start) > 17 THEN 'Evening'
    END
) AS `Part of the Day`,
(
    CASE
        WHEN g.duration <= 3 THEN 'Extra Short'
        WHEN g.duration BETWEEN 4 AND 6 THEN 'Short'
        WHEN g.duration BETWEEN 7 AND 10 THEN 'Long'
        ELSE 'Extra Long'
    END
) AS `Duration`
FROM games AS g;


USE `orders`;
# Problem 16 Orders Table
SELECT o.product_name, o.order_date,
DATE_ADD(o.order_date, INTERVAL 3 DAY) AS `pay_due`,
DATE_ADD(o.order_date, INTERVAL 1 MONTH ) AS `delivery_due`
FROM orders AS o;
