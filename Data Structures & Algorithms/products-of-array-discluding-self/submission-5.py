class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        out = [1] * len(nums)

        p = 1
        for i in range(1,len(nums)):
            p = nums[i-1]*p
            prefix[i] = p
        
        p = 1
        for i in range(len(nums)-2, -1, -1):
            p = nums[i+1]*p
            suffix[i] = p

        # print(f"prefix: {prefix}")
        # print(f"suffix: {suffix}")
        for i in range(len(nums)):
            out[i] = prefix[i]*suffix[i]
        
        return out