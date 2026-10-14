class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = defaultdict(int)
        maxc = (0, 0)

        for num in nums:
            
            d[num] += 1

            if d[num] > maxc[1]:
                maxc = (num, d[num])
        
        return maxc[0]

