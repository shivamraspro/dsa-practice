class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            ch_li = [0]*26
            for ch in s:
                ch_li[ord(ch)-ord('a')] += 1
            d[tuple(ch_li)].append(s)
        return list(d.values())