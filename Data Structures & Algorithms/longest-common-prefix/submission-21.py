class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ""
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                # print(f"i, j: {i}, {j}")
                # print(f"{strs[j][:i+1]}, {strs[0][:i+1]}")
                if strs[j][:i+1] != strs[0][:i+1]:
                    return strs[0][:i]
        return strs[0]
            