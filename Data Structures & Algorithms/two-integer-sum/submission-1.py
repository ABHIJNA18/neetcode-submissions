class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums[:-1]):
            dif=target-num1
            for j, num2 in enumerate(nums[i+1:]):
                if num2==dif:
                    return sorted([i,j+i+1])        
        