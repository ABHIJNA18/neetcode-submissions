class Solution:
    def isPalindrome(self, s: str) -> bool:

        newStr=''
        for char in s:
            if char.isalnum():
                newStr+=char.lower()
        return newStr[::-1]==newStr




        


        
        

        