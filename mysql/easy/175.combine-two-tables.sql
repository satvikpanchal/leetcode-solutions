# LeetCode Solution
# Problem: 175. Combine Two Tables
# Difficulty: Easy
# Language: Mysql
# URL: https://leetcode.com/problems/combine-two-tables/
# Submitted: 2025-09-29 03:20:22 UTC
# Status: Accepted

SELECT
  p.firstName,
  p.lastName,
  a.city,
  a.state
FROM Person AS p
LEFT JOIN Address AS a
  ON a.personId = p.personId;
