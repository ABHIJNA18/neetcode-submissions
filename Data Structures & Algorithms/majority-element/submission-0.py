class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map={}

        for num in nums:
            freq_map[num]= freq_map.get(num,0)+1
        
        #traverse the map
        for key, value in freq_map.items():
            if value > (len(nums)/2):
                return key
        