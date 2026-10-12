class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = ""
        for ch in s:
            if ((ord(ch) >= ord('a') and ord(ch) <= ord('z')) or 
            (ord(ch) >= ord('A') and ord(ch) <= ord('Z')) or 
            (ord(ch) >= ord('0') and ord(ch) <= ord('9'))):
                cs += ch.lower()
        
        i, j = 0, len(cs)-1
        while i < j:
            if cs[i] != cs[j]:
                return False
            i += 1
            j -= 1
        return True