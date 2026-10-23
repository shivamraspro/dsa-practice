class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        s.add(nums[0])
        i = 0
        j = 1
        while j < len(nums):
            if not nums[j] in s:
                i += 1
                nums[i] = nums[j]
                s.add(nums[j])
            
            j += 1
        return i+1