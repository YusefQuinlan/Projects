USE YqDbase;
CREATE TABLE OrderItems(
ItemNo int,
OrderNumber Varchar(255) ,
ItemQuantity int NOT NULL,
Price int NOT NULL,
Discount Varchar(255),
CONSTRAINT FK_ItemNo FOREIGN KEY (ItemNo)
REFERENCES items(ItemNo),
CONSTRAINT FK_OrderNumber FOREIGN KEY (OrderNumber)
REFERENCES clientorders(OrderNumber),
PRIMARY KEY (ItemNo,OrderNumber)
);