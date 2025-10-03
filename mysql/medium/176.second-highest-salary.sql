# LeetCode Solution
# Problem: 176. Second Highest Salary
# Difficulty: Medium
# Language: Mysql
# URL: https://leetcode.com/problems/second-highest-salary/
# Submitted: 2025-09-25 02:56:57 UTC
# Status: Accepted

# Write your MySQL query statement below
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);