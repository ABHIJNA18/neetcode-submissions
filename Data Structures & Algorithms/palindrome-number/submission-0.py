class Solution:
    def isPalindrome(self, x: int) -> bool:
        arr=str(x)
        l,r=0,len(arr)-1

        while l<r:
            if arr[l]==arr[r]:
                l+=1
                r-=1
            else:
                return False
        return True
        

        