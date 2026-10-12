class Solution:
    

    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonPrefix(str1, str2):
            if len(str1) > len(str2):
                str1, str2 = str2, str1
            prefix = ""
            for i in range(len(str1)):
                if str1[i] == str2[i]:
                    prefix += str1[i]
                else:
                    return prefix
            return prefix
            
        lcp = strs[0]
        for i in range(1, len(strs)):
            new_lcp = commonPrefix(lcp, strs[i])
            
            if new_lcp < lcp:
                lcp = new_lcp

        return lcp

        