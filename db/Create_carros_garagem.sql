USE garagem

CREATE TABLE carros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marca VARCHAR(255),
    modelo VARCHAR(255),
    ano INT
);

INSERT INTO carros (marca, modelo, ano) VALUES
( 'Toyota', 'Corolla', 2020),
( 'Honda', 'Civic', 2019),
( 'Ford', 'Focus', 2018),
( 'Chevrolet', 'Cruze', 2021),
( 'Volkswagen', 'Golf', 2017);
