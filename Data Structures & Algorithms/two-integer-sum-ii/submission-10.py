class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1
        while j < n:
            if numbers[i] + numbers[j] == target:
                return [i+1, j+1]
            
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i+1, j+1]