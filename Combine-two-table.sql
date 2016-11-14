'
Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId is the primary key column for this table.
Table: Address

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId is the primary key column for this table.

Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

FirstName, LastName, City, State
'
select FirstName,LastName,City,State from Person 
left join  Address on Person.PersonId = Address.PersonId;

# The 'left join' is combine two tables on the condition you set.
# It will create a table using the left table which is the Person with
# the each row. It will show null when the right-side table doesn't
# match the left table.
#The 'right join' is the same as left, the difference is the order.
