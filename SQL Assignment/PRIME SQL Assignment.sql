INSERT INTO Employee
(EmpId,FirstName,LastName,Department,Salary,HireData)
VALUES
(102,"Mark","Rivera","HR",4800,"2019-07-22"),
(103,"Sophia","Lee","Finance",4800,"2021-01-10"),
(104,"Daniel","Kim","IT",7200,"2018-11-05"),
(105,"Emma","Brown","Marketing",5800,"2022-04-18"),
(106,"Liam","Patel","Finance",5300,"2020-09-29"),
(107,"Olivia","Garcia","HR",6900,"2017-06-30"),
(108,"Noah","Thompson","IT",4600,"2023-02-12"),
(109,"Ava","Martinez","Marketing",7500,"2019-12-02"),
(110,"Ethan","Davis","Finance",5100,"2016-05-14");

#Q1
SELECT * FROM Employee;

#Q2
SELECT FirstName,LastName,Salary FROM Employee;

#Q3
SELECT * FROM Employee
WHERE Department IN ("IT");

#Q4
SELECT * FROM Employee
WHERE Salary > 6000;

#Q5
SELECT * FROM Employee
ORDER BY HireData DESC;

#Q6
SELECT DISTINCT(Department) FROM Employee;

#Q7
SELECT * FROM Employee
WHERE LEFT(FirstName, 1) IN ("A");

#Q8
SELECT * FROM Employee
WHERE salary BETWEEN 4000 AND 7000;

#Q9
SELECT AVG(salary) FROM Employee;

#Q10
SELECT Department,COUNT(EmpId) FROM Employee
GROUP BY Department
HAVING COUNT(EmpId) > 3