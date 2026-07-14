class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i, num in enumerate(nums):
            dif = target-num
            if dif in dict :
                return [dict[dif], i]
            dict[num] = i 

       
             
        