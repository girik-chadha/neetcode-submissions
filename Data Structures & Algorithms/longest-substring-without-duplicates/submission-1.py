class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,max_length=0,1
        sett=set()

        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        for R in range(len(s)):
            while s[R] in sett:
                sett.remove(s[L])
                L+=1
            sett.add(s[R])
            max_length=max(max_length,len(sett))
        return max_length
            
            
