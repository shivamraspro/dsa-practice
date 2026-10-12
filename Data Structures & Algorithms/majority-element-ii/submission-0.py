class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        res = set()
        for num in nums:
            if num in res:
                continue
            d[num] += 1
            if d[num] > len(nums)/3:
                res.add(num)
        return list(res)

        