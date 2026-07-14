class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)

        length=0
        for num in numSet:
            if (num-1) not in numSet:
                current_length=1
                while(num+current_length) in numSet:
                    current_length+=1
                length=max(length, current_length)
        return length
                
