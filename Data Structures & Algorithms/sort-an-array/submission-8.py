import random

class Solution:

    def partition(self, nums, st, en):
        pivot = nums[st]
        i = st
        for j in range(st+1, en+1):
            if nums[j] < pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[st], nums[i] = nums[i], nums[st]
        return i

    def qsort(self, nums, st, en):
        if st >= en:
            return
        
        pivot_idx = random.randint(st, en)
        nums[st], nums[pivot_idx] = nums[pivot_idx], nums[st]

        pivot = self.partition(nums, st, en)

        self.qsort(nums, st, pivot-1)
        self.qsort(nums, pivot+1, en)

    def sortArray(self, nums):
        self.qsort(nums, 0, len(nums)-1)
        return nums