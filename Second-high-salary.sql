'
Write a SQL query to get the second highest salary from the Employee table.

+----+--------+
| Id | Salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
For example, given the above Employee table, the second highest salary is 200. If there is no second highest salary, then the query should return null.
'
--solution 1 
select max(Salary) SecondHighestSalary  
from Employee where Salary < (select max(Salary) from Employee);
--This is based on the order of the salary.
--First we choose the biggest salary from the table 
--Then we select the second highest one.

--solution 2
select IFNULL( (select e.Salary from Employee e group by e.Salary order by 
	e.Salary desc limit 1, 1), NULL) SecondHighestSalary;



