# LeetCode Solution
# Problem: 2121. Find if Path Exists in Graph
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/find-if-path-exists-in-graph/
# Submitted: 2026-04-23 05:07:48 UTC
# Status: Accepted

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        res = 0
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        seen = set()
        def dfs(node):
            nonlocal res
            if node == destination:
                res +=1
                return

            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    dfs(nei)

        for i in range(n):
            if i not in seen and i == source:
                seen.add(i)
                dfs(i)

        return True if res else False


