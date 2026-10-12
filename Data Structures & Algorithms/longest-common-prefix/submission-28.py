class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""

        for i in range(len(strs[0])):
            ch = strs[0][i]
            for j in range(len(strs)):
                if i >= len(strs[j]) or ch != strs[j][i]:
                    return ans
            ans += ch
        
        return ans
