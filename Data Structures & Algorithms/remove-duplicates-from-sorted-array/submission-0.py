class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
            nums[k] = num
            k += 1
        return k