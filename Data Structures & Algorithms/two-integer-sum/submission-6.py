class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            tup = (num, target - num)
            if num > target - num:
                tup = (target - num, num)
            
            if tup in d:
                return [d[tup], i]
            else:
                d[tup] = i

       