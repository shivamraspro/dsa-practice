class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        st, en = 0, len(nums)-1
        i = 0

        while i <= en:
            if nums[i] == 0:
                nums[i], nums[st] = nums[st], nums[i]
                st += 1
            elif nums[i] == 2:
                nums[i], nums[en] = nums[en], nums[i]
                en -= 1
                i -= 1
            
            i += 1

        