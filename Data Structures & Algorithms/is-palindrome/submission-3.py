class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''

        for char in s:
            if char.isalnum():
                new_str += char.lower()

        i, j = 0, len(new_str) - 1

        while i < j:
            if new_str[i] == new_str[j]:
                i += 1
                j -= 1
            else:
                return False

        return True




        


        
        

        