CREATE DATABASE keacustomers;
USE keacustomers;

CREATE TABLE customers(
    cust_id INT(6) AUTO_INCREMENT PRIMARY KEY,
    cust_name VARCHAR(50),
    cust_email VARCHAR(50),
    cust_mobil VARCHAR(50)
);

INSERT INTO customers(cust_name, cust_email, cust_mobil)
VALUES(
    'Tue Hellstern',
    'tueh@kea.dk',
    '+45 12345678'
);

select * from customers;