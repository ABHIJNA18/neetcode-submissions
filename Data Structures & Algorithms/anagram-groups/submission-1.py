class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            countS=[0]*26
            for j in s:
                countS[ord(j)-ord("a")]+=1
            res[tuple(countS)].append(s)
        return list(res.values())


       
      


          




        