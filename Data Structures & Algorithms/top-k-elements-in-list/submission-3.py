class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        freq = [[] for i in range(len(nums) + 1)] #list comprehension

        for num in nums:
            freq_map[num]=1+ freq_map.get(num,0)
        
        for num, count in freq_map.items():
            freq[count].append(num)
            print(freq)
        print(freq)

        res=[]
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
       

        

        

