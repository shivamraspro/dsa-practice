class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(int)
        for i, num in enumerate(nums):
            print(num)
            print(d)
            diff = target - num
            if num in d:
                return [d[num], i]
            else:
                d[diff] = i
        return []
        