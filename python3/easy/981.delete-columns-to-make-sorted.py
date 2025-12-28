# LeetCode Solution
# Problem: 981. Delete Columns to Make Sorted
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/delete-columns-to-make-sorted/
# Submitted: 2025-12-20 00:39:42 UTC
# Status: Accepted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])
        
        delete_count = 0
        
        # Iterate through each column
        for c in range(cols):
            # Check each row in the current column
            for r in range(1, rows):
                # If the current character is lexicographically smaller 
                # than the previous one, the column is not sorted.
                if strs[r][c] < strs[r-1][c]:
                    delete_count += 1
                    break # Move to the next column immediately
                    
        return delete_count