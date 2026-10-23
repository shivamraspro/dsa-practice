class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        st, en = 0, len(nums)

        while st < en:
            if nums[st] == val:
                en -= 1
                nums[st] = nums[en]
                continue
            st += 1
        return en