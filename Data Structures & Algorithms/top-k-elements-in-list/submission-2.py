class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map={}
        for num in nums:
            freq_map[num]=1+ freq_map.get(num,0)
        #map is ready

        # sort it based on frequency and not the number
        #items returns (num, frequency) so you need (frequency, num) cuz sorted() takes first element from the pair 
        sortedS=[]
        for num, freq in freq_map.items():
            sortedS.append([freq,num])
        sortedS=sorted(sortedS)
        print(sortedS)

        arr=[]
        for i in range(k):
            arr.append(sortedS.pop()[1])
            print(arr)
        return arr
            

