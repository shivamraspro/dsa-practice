class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            sum = 0-n
            while j < k:
                if nums[j] + nums[k] < sum:
                    j += 1
                elif nums[j] + nums[k] > sum:
                    k -= 1
                else:
                    res.append([n, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res
        