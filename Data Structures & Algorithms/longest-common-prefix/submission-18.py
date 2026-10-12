class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(1, len(strs)):
                st = strs[j]
                if len(st) <= i:
                    return lcp
                if strs[j][i] != ch:
                    return lcp
            
            lcp += ch
        
        return lcp