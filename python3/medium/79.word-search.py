# LeetCode Solution
# Problem: 79. Word Search
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/word-search/
# Submitted: 2026-04-15 23:10:21 UTC
# Status: Accepted

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 or r > row - 1:
                return False
            if c < 0 or c > col - 1:
                return False

            if board[r][c] == "#":
                return False

            temp = board[r][c]
            
            if temp == word[i]:
                board[r][c] = "#"
                found = (backtrack(r - 1, c, i + 1) or
                         backtrack(r + 1, c, i + 1) or
                         backtrack(r, c - 1, i + 1) or
                         backtrack(r, c + 1, i + 1))

                board[r][c] = temp

                return found
            else:
                return False
        
        flag = False

        for r in range(0, row):
            for c in range(0, col):
                if board[r][c] == word[0]:
                    flag = backtrack(r, c, 0)
                
                if flag:
                    return True

        return False
