DELIMITER $$

CREATE PROCEDURE EmployeesSaleByMonth(
	month_nr int
)
BEGIN
	select 
		employees.LastName,
		orders.OrderID,
		month(orders.OrderDate) as 'monthnr',
		sum(orderdetails.Quantity * orderdetails.UnitPrice) as Total
	from employees join orders
	on employees.EmployeeID = orders.EmployeeID
	join orderdetails
	on orders.OrderID = orderdetails.OrderID
	group by employees.LastName, monthname(orders.OrderDate)
	having monthnr = month_nr
    order by Total desc;
END$$

DELIMITER ;

call EmployeesSaleByMonth(3);

