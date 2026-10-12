class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = sorted(strs)
        
        out = ""
        for i in range(len(s[0])):
            if (s[0][i] != s[len(s) - 1][i]):
                break
            out += s[0][i]
        return out
        

        