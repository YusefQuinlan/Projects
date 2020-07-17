CREATE DATABASE YqDbase;
USE YqDbase;
CREATE TABLE Clients(
ClientId varchar(255) PRIMARY KEY,
Firstname varchar(255) NOT NULL,
Lastname varchar(255) NOT NULL,
Email varchar(255),
PurchasedAmt int,
CurrentClient bool
);
