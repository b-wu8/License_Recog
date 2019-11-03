DROP DATABASE IF EXISTS Plates;
CREATE DATABASE Plates;
CONNECT Plates;

CREATE TABLE Plates (
    num    VARCHAR(8) PRIMARY KEY,
    make   VARCHAR(32),
    model  VARCHAR(32),
    car_color VARCHAR(32),
    owner_name VARCHAR(64),
    age    INTEGER,
    room   VARCHAR(32)
);

CREATE TABLE Admin (
    name    VARCHAR(32) PRIMARY KEY,
    clearance    CHAR(1)
);
