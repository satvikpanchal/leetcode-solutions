# LeetCode Solution
# Problem: 182. Duplicate Emails
# Difficulty: Easy
# Language: Mysql
# URL: https://leetcode.com/problems/duplicate-emails/
# Submitted: 2025-09-23 05:45:41 UTC
# Status: Accepted

# Write your MySQL query statement below
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
