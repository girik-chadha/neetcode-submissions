class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #edge cases
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        if len(s)==2 and  s[0]!=s[1]:
            return 2
        if len(s)==2 and  s[0]==s[1]:
            return 1
        
        L,R=0,0
        temp=set()
        maxx=0
        while R<len(s):
            if s[R] not in temp:
                temp.add(s[R])
                maxx=max(maxx,len(temp))
                R+=1
            elif s[R] in temp:
                temp.remove(s[L])
                L+=1

        return maxx
