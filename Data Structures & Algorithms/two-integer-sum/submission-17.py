class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in d:
                return [d[diff], i]
            
            d[nums[i]] = i