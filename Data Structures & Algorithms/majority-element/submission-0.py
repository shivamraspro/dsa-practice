class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = len(nums)/2
        d = defaultdict(int)
        for i in range(len(nums)):
            d[nums[i]] += 1
            if d[nums[i]] > check:
                return nums[i]

        