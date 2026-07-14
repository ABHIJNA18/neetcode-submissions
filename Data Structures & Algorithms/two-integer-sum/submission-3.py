class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices={}
        #fill in dict with value index pair 
        for i, num in enumerate(nums):
            indices[num]=i
        for i, num in enumerate(nums):
            dif = target-num
            #you should not compare the number with itself for example [3,3], hence the "and indices[diff]!=i:" 
            if dif in indices and indices[dif]!=i:
                return[i, indices[dif]]
        return []
        
        


       
             
        