SELECT * FROM [Customers] WHERE Country = 'UK';

SELECT COUNT(OrderID),CustomerName
FROM Orders
INNER JOIN Customers
ON Orders.CustomerID = Customers.CustomerID
GROUP BY CustomerName

SELECT SupplierName, MAX(AvgPrice)
FROM (
	SELECT SupplierName, AVG(Price) AS AvgPrice
    FROM Products
    INNER JOIN Suppliers
    ON Products.SupplierID = Suppliers.SupplierID
)

SELECT COUNT(DISTINCT Country)
FROM Customers

SELECT CategoryName, MaxCategory
FROM Categories
GROUP BY CategoryID
HAVING MAX(COUNT(CategoryID)) AS MaxCategory 
FROM (
    SELECT CategoryName, CategoryID
    FROM Categories
    INNER JOIN Products
    ON Categories.CategoryID = Products.CategoryID
    INNER JOIN OrderDetails
    ON Products.ProductID = OrderDetails.ProductID
)

SELECT EmployeeID, LastName, FirstName
FROM Employees
WHERE Notes IN 
(SELECT Notes FROM Employees WHERE Notes LIKE '%BS%')