class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            lcp = lcp + strs[0][i]
            # print(f"lcp is {lcp}")
            for j in range(len(strs)):
                # print(f"checking {strs[j][:i+1]}")
                if lcp != strs[j][:i+1]:
                    return lcp[:-1]
        return lcp