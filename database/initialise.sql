CREATE DATABASE products;

use products;

CREATE TABLE items_on_sale(
    name VARCHAR(24),
    qty INT(4),
    price INT(10)
);

INSERT INTO items_on_sale (name, qty, price) VALUES ('Muffins','4', '30'), ('Cake','20', '30'), ('Nails','100', '30'), ('harshit', '20', '30');