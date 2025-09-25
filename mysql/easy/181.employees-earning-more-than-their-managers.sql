# LeetCode Solution
# Problem: 181. Employees Earning More Than Their Managers
# Difficulty: Easy
# Language: Mysql
# URL: https://leetcode.com/problems/employees-earning-more-than-their-managers/
# Submitted: 2025-09-22 00:55:50 UTC
# Status: Accepted

# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
  ON e.managerId = m.id
WHERE e.salary > m.salary;
