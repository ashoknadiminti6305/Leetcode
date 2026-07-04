# Write your MySQL query statement below
SELECT 
 firstName,
 lastName,
 city,
 state
FROM Person
left join address
on person.personId = Address.personId;