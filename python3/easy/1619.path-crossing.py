# LeetCode Solution
# Problem: 1619. Path Crossing
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/path-crossing/
# Submitted: 2025-10-21 23:58:56 UTC
# Status: Accepted

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        if len(path) <= 1:
            return False

        visited = set()
        x, y = 0, 0
        visited.add((x, y)) 

        for i in path:
            if i == "N":
                y += 1
            elif i == "S":
                y -= 1
            elif i == "E":
                x += 1          
            elif i == "W":
                x -= 1          

            if (x, y) in visited:  
                return True
            visited.add((x, y))    

        return False
