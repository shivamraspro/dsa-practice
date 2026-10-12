class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for num in s:
            long = 0
            curr = num
            if (curr - 1) not in s:
                long += 1
                while num + 1 in s:
                    long += 1
                    num = num + 1
            if long > longest:
                longest = long

        return longest
