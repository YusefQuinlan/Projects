USE YqDbase;
CREATE TABLE ClientOrders(
OrderNumber varchar(255),
ClientId varchar(255) ,
CONSTRAINT FK_ClientOrders FOREIGN KEY (ClientId) REFERENCES  clients(ClientId),
CONSTRAINT PK_clientorders PRIMARY KEY (OrderNumber, ClientId)
);
