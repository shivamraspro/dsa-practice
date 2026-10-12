class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set()
        for num in nums:
            numset.add(num)
        
        maxcount = 0
        for num in nums:
            if num-1 in numset:
                continue
            
            count = 0
            candidate = num
            while candidate in numset:
                count += 1
                candidate += 1
            
            if count > maxcount:
                maxcount = count
        
        return maxcount