class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0

        i=0
        j=len(heights)-1

        while(i<j):
            cur_area=min(heights[i],heights[j])*(j-i)
            print(cur_area)
            max_area=max(cur_area,max_area)
            print(max_area)
            #incrementing logic 
            if heights[i]<=heights[j]:
                i+=1
            else:
                j-=1
        return max_area



            

        