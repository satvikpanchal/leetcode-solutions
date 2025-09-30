# LeetCode Solution
# Problem: 184. Department Highest Salary
# Difficulty: Medium
# Language: Mysql
# URL: https://leetcode.com/problems/department-highest-salary/
# Submitted: 2025-09-30 02:44:41 UTC
# Status: Accepted

# Write your MySQL query statement below
SELECT
  d.name AS Department,
  e.name AS Employee,
  e.salary AS Salary
FROM Employee e
JOIN Department d
  ON d.id = e.departmentId
WHERE e.salary = (
  SELECT MAX(salary)
  FROM Employee
  WHERE departmentId = e.departmentId
);
