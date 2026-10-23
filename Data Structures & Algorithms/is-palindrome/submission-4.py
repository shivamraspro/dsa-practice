class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, n = 0, len(s)-1
        while i < n:
            if not s[i].isalnum():
                i += 1
                continue
            if not s[n].isalnum():
                n -= 1
                continue
            
            if s[i].lower() != s[n].lower():
                return False
            
            i += 1
            n -= 1
        return True