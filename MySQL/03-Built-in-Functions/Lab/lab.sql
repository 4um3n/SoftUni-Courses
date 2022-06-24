USE `book_library`;


# Problem 1 Find Book Titles
SELECT `b`.`title`
FROM `books` AS `b`
WHERE `b`.`title` LIKE 'The%'
ORDER BY `b`.`id`;


# Problem 2 Replace Titles
SELECT REPLACE(`b`.`title`, 'The', '***')
FROM `books` AS `b`
WHERE `b`.`title` LIKE 'The%'
ORDER BY `b`.`id`;


# Problem 3 Sum Cost Of All Books
SELECT CONVERT(SUM(b.cost), DECIMAL(6, 2)) as `prices`
FROM books AS b;


# Problem 4 Days Lived
SELECT CONCAT(a.first_name, ' ', a.last_name) AS `Full Name`  ,DATEDIFF(a.died, a.born) AS `Days Lived`
FROM authors as a;


# Problem 5 Harry Potter Books
SELECT b.title
FROM books as b
WHERE b.title LIKE '%Harry Potter%'
ORDER BY b.id;
