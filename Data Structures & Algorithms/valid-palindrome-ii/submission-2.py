class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(l, r, deleted):
            if l > r:
                return False
            
            while l < r:
                if s[l] != s[r]:
                    if deleted:
                        return False    
        
                    if s[l] == s[r-1] or s[l+1] == s[r]:
                        return isPalindrome(l, r-1, True) or isPalindrome(l+1, r, True)
                    else:
                        return False
                l += 1
                r -= 1
            return True

        return isPalindrome(0, len(s)-1, False)