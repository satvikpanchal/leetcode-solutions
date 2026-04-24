# LeetCode Solution
# Problem: 323. Number of Connected Components in an Undirected Graph
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Submitted: 2026-04-23 05:13:09 UTC
# Status: Accepted

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()
        res = 0

        def dfs(node):
            for n in graph[node]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)

        for i in range(0, n):
            if i not in seen:
                res += 1
                seen.add(i)
                dfs(i)

        return res