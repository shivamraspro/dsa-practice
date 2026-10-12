class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for i in s:
            if i.isalnum():
                r += i.lower()
        print(r)
        i, j = 0, len(r)-1
        while i <= j:    
            if r[i] != r[j]:
                return False
            i += 1
            j -= 1
        return True
        