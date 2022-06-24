# SET UP
CREATE DATABASE IF NOT EXISTS gamebar;
USE gamebar;


# Problem 1 Create Tables
CREATE TABLE employees (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE categories (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);

CREATE TABLE products (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(30) NOT NULL,
    category_id INT NOT NULL
);


# Problem 2 Insert Data In Tables
INSERT INTO employees (first_name, last_name)
VALUES ('Test', 'Testov');

INSERT INTO employees (first_name, last_name)
VALUES ('Test1', 'Test1');

INSERT INTO employees (first_name, last_name)
VALUES ('Test2', 'Test3');


# Problem 3 Alter Table
ALTER TABLE `employees`
ADD COLUMN `middle_name` VARCHAR(50) NOT NULL;


# Problem 4 Adding Constraints
ALTER TABLE `products`
ADD CONSTRAINT `fk_products_categories`
FOREIGN KEY (`category_id`) REFERENCES categories(`id`);


# Problem 5 Modifying Columns
ALTER TABLE `employees`
MODIFY COLUMN `middle_name` VARCHAR(100);
