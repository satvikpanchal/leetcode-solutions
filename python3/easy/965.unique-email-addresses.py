# LeetCode Solution
# Problem: 965. Unique Email Addresses
# Difficulty: Easy
# Language: Python3
# URL: https://leetcode.com/problems/unique-email-addresses/
# Submitted: 2026-05-05 01:58:31 UTC
# Status: Accepted

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
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