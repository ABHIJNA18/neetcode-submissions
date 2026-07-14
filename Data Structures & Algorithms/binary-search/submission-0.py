class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1

        while l<=r:
            m=(l+r)//2 # not len(nums)//2
            if target > nums[m]:
                l=m+1
            elif target < nums[m]:
                r=m-1
            else:
                #means its not greater or lessser, so must be the equal 
                return m
        return -1


        