class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        map_nums={}
        for i, num in enumerate(nums):
            map_nums[num] = i
        print(map_nums)

        seq_array=[]
        for num in nums:
            if (num-1) in map_nums:
                continue
            else:
                seq_array.append(num)
        print(seq_array)

        if len(seq_array)==0:
            return 0
        count_freq=[0]*len(seq_array)
        print(count_freq)

        for j,n in enumerate(seq_array):
            count,i=1,1
            while (n+i) in map_nums:
                count+=1
                i+=1
            count_freq[j]=count
        print(count_freq)
        
        sorted_freq=sorted(count_freq)
        print(sorted_freq)
        f=sorted_freq.pop()
        return f
            


