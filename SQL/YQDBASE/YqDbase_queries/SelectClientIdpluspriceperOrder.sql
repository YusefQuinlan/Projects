USE Yqdbase;
SELECT clientorders.OrderNumber AS "Order", ClientId, Price
FROM clientorders, orderitems
WHERE clientorders.OrderNumber = orderitems.OrderNumber;