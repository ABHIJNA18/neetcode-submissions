class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_1=set(nums)
        if(len(nums_1)!=len(nums)):
            return True
        else:
            return False
