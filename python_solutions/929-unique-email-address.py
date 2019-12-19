# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            seen.add(local.replace('.','') + '@' + domain)
        return len(seen)
        
"""
Runtime: 48 ms, faster than 91.55% of Python3 online submissions for Unique Email Addresses.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Unique Email Addresses.
"""
