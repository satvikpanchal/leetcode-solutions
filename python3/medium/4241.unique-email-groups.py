# LeetCode Solution
# Problem: 4241. Unique Email Groups
# Difficulty: Medium
# Language: Python3
# URL: https://leetcode.com/problems/unique-email-groups/
# Submitted: 2026-05-05 01:57:13 UTC
# Status: Accepted

class Solution:
    def uniqueEmailGroups(self, emails: list[str]) -> int:
        res = defaultdict(set)
        emails_res = 0

        for i in emails:
            user, domain = i.split("@")

            normalized = ""
            for j in user:
                if j == ".": 
                    continue
                
                if j == "+":
                    break

                normalized += j.lower()
            
            res[domain.lower()].add(normalized)
        
        for k, v in res.items():
            emails_res += len(v)
        
        return emails_res
            
