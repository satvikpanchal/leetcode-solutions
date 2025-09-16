# LeetCode Solution
# Problem: 1908. Recyclable and Low Fat Products
# Difficulty: Easy
# Language: Mysql
# URL: https://leetcode.com/problems/recyclable-and-low-fat-products/
# Submitted: 2025-06-25 21:09:36 UTC
# Status: Accepted

# Write your MySQL query statement below
SELECT product_id FROM products
WHERE low_fats = 'Y' AND recyclable = 'Y';