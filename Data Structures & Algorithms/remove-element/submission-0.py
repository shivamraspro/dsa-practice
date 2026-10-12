class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, j = 0, 0
        while j < len(nums):
            if i == j and nums[j] != val:
                i += 1
                j += 1
            elif i == j and nums[j] == val:
                j += 1
            elif i != j and nums[j] != val:
                nums[i] = nums[j]
                i += 1
                j += 1
            elif i != j and nums[j] == val:
                j += 1

        return i
        