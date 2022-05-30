# Set Up
CREATE DATABASE IF NOT EXISTS `minions`;
USE `minions`;


# Problem 1 Create Tables
CREATE TABLE `minions` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30) NOT NULL,
    `age` INT
);

CREATE TABLE `towns` (
    `town_id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30) NOT NULL,
    `picture` BLOB
);


# Problem 2 Alter Minions Table
ALTER TABLE `towns`
RENAME COLUMN `town_id` TO `id`;

ALTER TABLE `minions`
ADD COLUMN `town_id` INT NOT NULL;

ALTER TABLE `minions`
ADD CONSTRAINT `fk_minions_towns`
FOREIGN KEY (`town_id`) REFERENCES `towns`(`id`);


# Problem 3 Insert Records In Both Tables
INSERT INTO `towns`
VALUES
(1, 'Sofia', null),
(2, 'Plovdiv', null),
(3, 'Varna', null);

INSERT INTO `minions`
VALUES
(1, 'Kevin', 22, 1),
(2, 'Bob', 15, 3),
(3, 'Steward', null, 2);


# Problem 4 Truncate Table Minions
TRUNCATE TABLE `minions`;


# Problem 5 Drop All Tables
DROP TABLE IF EXISTS `minions`, `towns`;


# Problem 6 Create Table People
CREATE TABLE `people` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(200) NOT NULL,
    `picture` BLOB,
    `height` FLOAT(5, 2),
    `weight` FLOAT(5, 2),
    `gender` CHAR(1) NOT NULL,
    `birthdate` DATE NOT NULL,
    `biography` TEXT
);

INSERT INTO `people`
VALUES
(DEFAULT, 'Bla', null, null, null, 'm', '1990-10-10', null),
(DEFAULT, 'Bla', null, null, null, 'm', '1990-10-10', null),
(DEFAULT, 'Bla', null, null, null, 'm', '1990-10-10', null),
(DEFAULT, 'Bla', null, null, null, 'm', '1990-10-10', null),
(DEFAULT, 'Bla', null, null, null, 'm', '1990-10-10', null);


# Problem 7 Create Table Users
CREATE TABLE `users` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `username` VARCHAR(30) NOT NULL,
    `password` VARCHAR(26) NOT NULL,
    `profile_picture` BLOB,
    `last_login_time` DATETIME,
    `is_deleted` BOOL NOT NULL
);

INSERT INTO `users`
VALUES
(DEFAULT, 'az', 'bla', null, null, false),
(DEFAULT, 'az1', 'bla', null, null, false),
(DEFAULT, 'az2', 'bla', null, null, false),
(DEFAULT, 'az3', 'bla', null, null, false),
(DEFAULT, 'az4', 'bla', null, null, false);


# Problem 8 Change Primary Key
ALTER TABLE `users`
DROP PRIMARY KEY,
ADD CONSTRAINT `pk_users`
PRIMARY KEY (`id`, `username`);


# Problem 9 Set Default Value Of Field
ALTER TABLE `users`
MODIFY `last_login_time` DATETIME DEFAULT NOW();

# Problem 10 Set Unique Field
ALTER TABLE `users`
DROP PRIMARY KEY,
ADD CONSTRAINT `pk_users`
PRIMARY KEY (`id`),
MODIFY COLUMN `username` VARCHAR(30) UNIQUE NOT NULL;


# Problem 11 Movies Database
CREATE SCHEMA IF NOT EXISTS `movies`;
USE `movies`;

CREATE TABLE `directors` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `director_name` VARCHAR(30) NOT NULL,
    `notes` TEXT
);

INSERT INTO `directors` (`director_name`, `notes`)
VALUES
('Name', null),
('Name', null),
('Name', null),
('Name', null),
('Name', null);

CREATE TABLE `genres` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `genre_name` VARCHAR(30) NOT NULL,
    `notes` TEXT
);

INSERT INTO `genres` (genre_name, notes)
VALUES
('Genre Name', null),
('Genre Name', null),
('Genre Name', null),
('Genre Name', null),
('Genre Name', null);

CREATE TABLE `categories` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `category_name` VARCHAR(30) NOT NULL,
    `notes` TEXT
);

INSERT INTO `categories` (category_name, notes)
VALUES
('Category Name', null),
('Category Name', null),
('Category Name', null),
('Category Name', null),
('Category Name', null);

CREATE TABLE `movies` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `title` VARCHAR(50) NOT NULL,
    `director_id` INT NOT NULL,
    `copyright_year` DATE NOT NULL,
    `length` INT NOT NULL,
    `genre_id` INT NOT NULL,
    `category_id` INT NOT NULL,
    `rating` FLOAT(3, 2) NOT NULL,
    `notes` TEXT
);

INSERT INTO `movies`
VALUES
(DEFAULT, 'Movie', 1, NOW(), 135, 1, 1, 9.1, null),
(DEFAULT, 'Movie', 2, NOW(), 135, 2, 2, 9.1, null),
(DEFAULT, 'Movie', 3, NOW(), 135, 3, 3, 9.1, null),
(DEFAULT, 'Movie', 4, NOW(), 135, 4, 4, 9.1, null),
(DEFAULT, 'Movie', 5, NOW(), 135, 5, 5, 9.1, null);


# Problem 12 Car Rental Database
CREATE SCHEMA IF NOT EXISTS `car_rental`;
USE `car_rental`;

CREATE TABLE `categories` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `category` VARCHAR(30) NOT NULL,
    `daily_rate` FLOAT(3,2),
    `weekly_rate` FLOAT(3,2),
    `monthly_rate` FLOAT(3,2),
    `weekend_rate` FLOAT(3,2)
);

INSERT INTO `categories`
VALUES
(DEFAULT, 'Category', null, null, null, null),
(DEFAULT, 'Category', null, null, null, null),
(DEFAULT, 'Category', null, null, null, null);


CREATE TABLE `cars` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `plate_number` VARCHAR(10) NOT NULL,
    `make` VARCHAR(15) NOT NULL,
    `model` VARCHAR(15) NOT NULL,
    `car_year` DATE NOT NULL,
    `category_id` INT,
    `doors` INT NOT NULL,
    `picture` BLOB,
    `car_condition` VARCHAR(15) NOT NULL,
    `available` BOOL NOT NULL
);

ALTER TABLE `cars`
ADD CONSTRAINT `fk_cars_categories`
FOREIGN KEY (`category_id`) REFERENCES `categories`(`id`);

INSERT INTO `cars`
VALUES
(DEFAULT, 'CA0000CA', 'Subaru', 'Impreza', NOW(), 1, 2, null, 'excellent', TRUE),
(DEFAULT, 'CA0000CA', 'Subaru', 'Impreza', NOW(), 1, 2, null, 'excellent', TRUE),
(DEFAULT, 'CA0000CA', 'Subaru', 'Impreza', NOW(), 1, 2, null, 'excellent', TRUE);

CREATE TABLE `employees` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(30) NOT NULL,
    `last_name` VARCHAR(30) NOT NULL,
    `title` VARCHAR(50),
    `notes` TEXT
);

INSERT INTO `employees`
VALUES
(DEFAULT, 'Pesho', 'Pesho', null, null),
(DEFAULT, 'Pesho', 'Pesho', null, null),
(DEFAULT, 'Pesho', 'Pesho', null, null);


CREATE TABLE `customers` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `driver_licence_number` INT NOT NULL,
    `full_name` VARCHAR(50) NOT NULL,
    `address` VARCHAR(50) NOT NULL,
    `city` VARCHAR(35) NOT NULL,
    `zip_code` INT NOT NULL,
    `notes` TEXT
);

INSERT INTO `customers`
VALUES
(DEFAULT, 10101010, 'Bla Bla', 'Bla@Bla No 3', 'Blaaaa', 1000, null),
(DEFAULT, 10101010, 'Bla Bla', 'Bla@Bla No 3', 'Blaaaa', 1000, null),
(DEFAULT, 10101010, 'Bla Bla', 'Bla@Bla No 3', 'Blaaaa', 1000, null);


CREATE TABLE `rental_orders` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `employee_id` INT NOT NULL,
    `customer_id` INT NOT NULL,
    `car_id` INT NOT NULL,
    `car_condition` VARCHAR(15) NOT NULL,
    `tank_level` INT NOT NULL,
    `kilometrage_start` INT NOT NULL,
    `kilometrage_end` INT NOT NULL,
    `total_kilometrage` INT NOT NULL,
    `start_date` DATE NOT NULL,
    `end_date` DATE NOT NULL,
    `total_days` INT NOT NULL,
    `rate_applied` FLOAT(3, 2),
    `tax_rate` FLOAT(3, 2),
    `order_status` VARCHAR(15) NOT NULL,
    `notes` TEXT
);

ALTER TABLE `rental_orders`
ADD CONSTRAINT `fk__employee_id__employees__id`
FOREIGN KEY (`employee_id`) REFERENCES `employees`(`id`),
ADD CONSTRAINT `fk__customer_id__customers__id`
FOREIGN KEY (`customer_id`) REFERENCES `customers`(`id`),
ADD CONSTRAINT `fk__car_id__cars__id`
FOREIGN KEY (`car_id`) REFERENCES  `cars`(`id`);


INSERT INTO `rental_orders`
VALUES
(DEFAULT, 1, 1, 1, 'good', 30, 150000 , 210000, 60000, NOW(), NOW(), 0, 9.1, 5, 'completed', null),
(DEFAULT, 1, 1, 1, 'good', 30, 150000 , 210000, 60000, NOW(), NOW(), 0, 9.1, 5, 'completed', null),
(DEFAULT, 1, 1, 1, 'good', 30, 150000 , 210000, 60000, NOW(), NOW(), 0, 9.1, 5, 'completed', null);


# Problem 13 Basic Inserts
CREATE SCHEMA IF NOT EXISTS `soft_uni`;
USE `soft_uni`;

CREATE TABLE `towns` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(50) NOT NULL
);

CREATE TABLE `addresses` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `address_text` VARCHAR(50) NOT NULL,
    `town_id` INT NOT NULL
);

ALTER TABLE `addresses`
ADD CONSTRAINT `fk__town_id__towns__id`
FOREIGN KEY (`town_id`) REFERENCES `towns`(`id`);

CREATE TABLE `departments` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `name` VARCHAR(30) NOT NULL
);

CREATE TABLE `employees` (
    `id` INT AUTO_INCREMENT PRIMARY KEY,
    `first_name` VARCHAR(30) NOT NULL,
    `middle_name` VARCHAR(30),
    `last_name` VARCHAR(30) NOT NULL,
    `job_title` VARCHAR(40) NOT NULL,
    `department_id` INT NOT NULL,
    `hire_date` DATE NOT NULL,
    `salary` FLOAT(7, 3) NOT NULL,
    `address_id` INT NOT NULL
);

ALTER TABLE `employees`
ADD CONSTRAINT `fk__department_id__departments__id`
FOREIGN KEY (`department_id`) REFERENCES `departments`(`id`),
ADD CONSTRAINT `fk__address_id__addresses__id`
FOREIGN KEY (`address_id`) REFERENCES `addresses`(`id`);

INSERT INTO `towns` (name)
VALUES
('Sofia'),
('Plovdiv'),
('Varna'),
('Burgas');

INSERT INTO `departments` (name)
VALUES
('Engineering'),
('Sales'),
('Marketing'),
('Software Development'),
('Quality Assurance');

INSERT INTO `addresses` (address_text, town_id)
VALUES
('Sofia', 1),
('Plovdiv', 2),
('Varna', 3),
('Burgas', 4);

INSERT INTO `employees`
VALUES
(DEFAULT, 'Ivan', 'Ivanov', 'Ivanov', '.NET Developer', 4, '2013-02-01', 3500, 1),
(DEFAULT, 'Petar', 'Petrov', 'Petrov', 'Senior Engineer', 1, '2004-03-02', 4000, 2),
(DEFAULT, 'Maria', 'Petrova', 'Ivanova', 'Intern', 5, '2016-08-28', 525.25, 3),
(DEFAULT, 'Georgi', 'Terziev', 'Ivanov', 'CEO', 2, '2007-12-09', 3000, 4),
(DEFAULT, 'Peter', 'Pan', 'Pan', 'Intern', 3, '2016-08-28', 599.88, 1);


# Problem 14 Basic Select All Fields
SELECT * FROM `towns`;
SELECT * FROM `departments`;
SELECT * FROM `employees`;


# Problem 15 Basic Select All Fields And Order Them
SELECT * FROM `towns`
ORDER BY `name`;

SELECT * FROM `departments`
ORDER BY `name`;

SELECT * FROM `employees`
ORDER BY `salary` DESC;


# Problem 16 Basic Select Some Fields
SELECT `name`
FROM `towns`
ORDER BY `name`;

SELECT `name`
FROM `departments`
ORDER BY `name`;

SELECT `first_name`, `last_name`, `job_title`, `salary`
FROM `employees`
ORDER BY `salary` DESC;


# Problem 17 Increase Employees Salary
UPDATE `employees`
SET `salary` = `salary` + `salary` * 0.10;

SELECT `salary`
FROM employees;


# Problem 18 Delete All Records
TRUNCATE TABLE `occupancies`;
