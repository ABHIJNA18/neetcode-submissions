class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product=1
        for i,num in enumerate(nums):
            if num ==0:
                continue
            else :
                product*=num
        print(product)
        count=0
        for i, num in enumerate(nums):
            if num==0:
                count+=1
        print(count)
        #if count = 1 , then list has all 0 except at 0's index
        # if count more than 1,everything is 0
        if count > 1:
            return [0]*len(nums)
        elif count ==1 :
            res=[0]*(len(nums)-1)
            for i in range(len(nums)):
                if nums[i] != 0:
                    continue
                res.insert(i,product)
            return res
        else:
            res=[]
            for i in range(len(nums)):
                prod=product//nums[i]
                res.append(prod)
            return res
        

        