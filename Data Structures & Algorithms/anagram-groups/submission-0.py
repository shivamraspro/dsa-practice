class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def validAnagram(str1, str2):
            if len(str1) != len(str2):
                return False
            
            d1, d2 = {}, {}
            for i in range(len(str1)):
                d1[str1[i]] = d1[str1[i]] + 1 if str1[i] in d1 else 0
                d2[str2[i]] = d2[str2[i]] + 1 if str2[i] in d2 else 0
            
            return d1 == d2

        groups = []

        for s in strs:
            # print(f"s is {s}")
            # print(f"groups is {groups}")
            flag = False
            for i in range(len(groups)):
                g = groups[i]
                # print(f"{g[0]} and {s} are valid anagrams: {validAnagram(g[0], s)}")
                if len(g) > 0 and validAnagram(g[0], s):
                    g.append(s)
                    flag = True

            if flag == False:
                groups.append([s])
            # print(f"groups is {groups}")
        
        return groups
            

