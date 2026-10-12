class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        maxlarr = [0]*len(height)
        maxrarr = [0]*len(height)

        lastmax = 0
        for i in range(len(height)):
            lastmax = max(lastmax, height[i])
            maxlarr[i] = lastmax
        
        lastmax = 0
        for i in range(len(height)-1, -1, -1):
            lastmax = max(lastmax, height[i])
            maxrarr[i] = lastmax

        # print(f"maxlarr: {maxlarr}")
        # print(f"maxrarr: {maxrarr}")
        res = 0
        for i in range(len(height)):
            res += min(maxlarr[i], maxrarr[i]) - height[i]
        
        return res