# LeetCode Solution
# Problem: 2445. Reachable Nodes With Restrictions
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/reachable-nodes-with-restrictions/
# Submitted: 2026-04-24 05:04:51 UTC
# Status: Accepted

class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        restricted = set(restricted)
        seen = set()
        res = 0

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node):
            nonlocal res
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted:
                    seen.add(neighbor)
                    res += 1
                    dfs(neighbor)

        seen.add(0)
        res = 1
        dfs(0)

        return res

