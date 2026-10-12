class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i, j = 0, n-1
        res = 0
        mins = prices[0]
        for i in range(1, n):
            curr = prices[i]
            diff = curr - mins

            if diff > res:
                res = diff

            if curr < mins:
                mins = curr
        return res