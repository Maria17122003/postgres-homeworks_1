-- SQL-команды для создания таблиц
CREATE DATABASE north

CREATE TABLE customers_data
(
	customer_id	int PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);

CREATE TABLE employees_data
(
	first_name	varchar(50) PRIMARY KEY,
	last_name varchar(50),
	title varchar(100),
	birth_date date,
	notes text
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(50) REFERENCES customers_data(customer_id),
	employee_id varchar(100),
	order_date date,
	ship_city text
);
