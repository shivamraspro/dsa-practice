class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        
        res = []
        for key in d.keys():
            res.append((key, d[key]))
        
        res = sorted(res, key= lambda x: x[1])
        
        return list(map(lambda x: x[0], res[-1*k:]))
        
        

        