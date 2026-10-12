class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        d = defaultdict(int)
        for i in range(len(s)):
            d[s[i]] += 1
            d[t[i]] -= 1
        
        s = set(d.values())
        return len(s) == 1 and s == {0,}