DROP TABLE IF EXISTS Guitars;
create table Guitars(
    id INT primary key,
    brand varchar,
    name varchar,
    price numeric,
    finish varchar
);
  
INSERT INTO Guitars (id, brand, name, price, finish)VALUES
(1 ,'Gibson' ,'70s Flying V' ,2499.00 ,'Classic White' ),
(2 ,'ESP' ,'SnakeByte' ,1499.00 ,'Snow White' ),
(3 ,'Shecter' ,'Synyster Gates Custom-S' ,1599.00 ,'Gloss Black with Silver Stripes' ),
(4 ,'Jackson' ,'Rhoads JS32T' ,469.99 ,'White with Black Bevels' ),
(5 ,'Fender' ,'Player II Stratocaster HSS' ,999.99 ,'Transparent Cherry Burst with Rosewood Fingerboard' ),
(6 ,'PRS','SE Studio',1099.00 ,'Charcoal Cherry Burst'),
(7,'Fender', 'American Professional II jazzmaster', 1739.99, 'Dark Night with Rosewood Fingerboard'),
(8, 'Epiphone', 'SG Custom Electric Guitar', 699.00, 'Alpine White'),
(9,'Ibanez', 'Prestige RG652AHM', 1799.99, 'Antique White'),
(10,'ESP', 'Kirk Hammett Signature White Zombie', 1619.10, 'Black with Graphic');

SELECT id, brand, name, to_char(price, '"$"99,999.00') AS price, finish from Guitars;
  


