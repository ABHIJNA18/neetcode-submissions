class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1

        while l<r:
            m= (l+r)//2
            if nums[m] > nums[r]: # this means somehwre on the right the seperation is present, so discard left half 
                l=m+1
            elif nums[m] < nums[r]: # this means the seperation happened in left
                r=m
        return nums[l]
        
                  
        