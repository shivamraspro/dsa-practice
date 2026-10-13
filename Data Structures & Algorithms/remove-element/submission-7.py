class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last, curr = 0, 0
        while curr < len(nums):
            if nums[curr] == val:
                curr += 1
                continue
            nums[last] = nums[curr]
            curr += 1
            last += 1

        return last