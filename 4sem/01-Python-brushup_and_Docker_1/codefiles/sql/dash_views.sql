# VIEWS
# Tue Hellstern

# CategorySale
create view CategorySale
as
	select 
		CategoryName,
		sum(orderdetails.UnitPrice * orderdetails.Quantity) as Total
	from categories join products
	on categories.CategoryID = products.ProductID
	join orderdetails
	on products.ProductID = orderdetails.ProductID
	group by CategoryName
	order by total desc;

# EmployeesSale
create view EmployeesSale
as
	select 
    concat(employees.FirstName, ' ', employees.LastName) as EmployeeName,
    sum(orderdetails.UnitPrice * orderdetails.Quantity) as Total
    from employees join orders
    on employees.EmployeeID = orders.EmployeeID
    join orderdetails
    on orders.OrderID = orderdetails.OrderID
    group by FirstName
	order by Total desc;    
    
# Top5Products
create view Top5Products
as
	select 
    ProductName,
    sum(orderdetails.UnitPrice * orderdetails.Quantity) as Total
    from products join orderdetails
    on products.ProductID = orderdetails.ProductID
    group by ProductName
    order by Total desc
	LIMIT 5;
    
# Top5Customers
create view Top5Customers
as
    SELECT 
        `customers`.`CompanyName` AS `CompanyName`,
        SUM((`orderdetails`.`UnitPrice` * `orderdetails`.`Quantity`)) AS `Total`
    FROM
        ((`customers`
        JOIN `orders` ON ((`customers`.`CustomerID` = `orders`.`CustomerID`)))
        JOIN `orderdetails` ON ((`orders`.`OrderID` = `orderdetails`.`OrderID`)))
    GROUP BY `customers`.`CompanyName`
    ORDER BY `Total` DESC
    LIMIT 5