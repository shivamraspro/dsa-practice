class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            arr = [0]*26
            for ch in s:
                arr[ord(ch)-ord('a')] += 1
            arr_tup = tuple(arr)
            if arr_tup in d:
                d[arr_tup].append(s)
            else:
                d[arr_tup] = [s]
        
        res = []
        for ix, key in enumerate(d):
            res.append(d[key])
        return res