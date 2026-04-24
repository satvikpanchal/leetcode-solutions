# LeetCode Solution
# Problem: 547. Number of Provinces
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-provinces/
# Submitted: 2026-04-23 00:22:53 UTC
# Status: Accepted

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        seen = set()
        n = len(isConnected)

        def dfs(node):
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)

        for i in range(0, n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        print(graph)

        res = 0

        for i in range(0, n):
            if i not in seen:
                res += 1
                seen.add(i)
                dfs(i)

        return res


