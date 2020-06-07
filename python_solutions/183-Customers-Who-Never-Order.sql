select customers.name as 'Customers'
from Customers
where Customers.id not in
(
    select CustomerId from Orders
);