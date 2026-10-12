class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        can = nums[0]
        count = 0
        for i in range(len(nums)):
            if count == 0:
                can = nums[i]
                
            if nums[i] == can:
                count += 1
            else:
                count -=1

            
            
        return can