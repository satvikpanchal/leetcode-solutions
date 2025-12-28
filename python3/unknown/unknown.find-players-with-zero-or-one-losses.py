# LeetCode Solution
# Problem: unknown. Find Players With Zero or One Losses
# Difficulty: Unknown
# Language: Python3
# URL: https://leetcode.com/problems/find-players-with-zero-or-one-losses/
# Submitted: 2025-12-09 02:00:56 UTC
# Status: Accepted

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}

        # count losses for all players
        for winner, loser in matches:
            if winner not in losses:
                losses[winner] = 0
            if loser not in losses:
                losses[loser] = 0
            losses[loser] += 1
        
        zero_loss = []
        one_loss = []

        for player in losses:
            if losses[player] == 0:
                zero_loss.append(player)
            elif losses[player] == 1:
                one_loss.append(player)
        
        return [sorted(zero_loss), sorted(one_loss)]
            