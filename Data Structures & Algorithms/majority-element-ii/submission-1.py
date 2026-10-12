class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        res = []
        for num in nums:
            if d[num] == -1:
                continue
            d[num] += 1
            if d[num] > len(nums) // 3:
                res.append(num)
                d[num] = -1
        return res