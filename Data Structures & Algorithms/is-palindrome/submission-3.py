class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        while i <= j:
            ich, jch = s[i], s[j]
            if not ich.isalnum():
                i += 1
                continue
            elif not jch.isalnum():
                j -= 1
                continue
            elif ich.lower() == jch.lower():
                i += 1
                j -= 1
                continue
            else:
                return False
        return True