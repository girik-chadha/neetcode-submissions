class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if s == " ":
            return 1

        L, R = 0, 0
        sett = set()
        maxL=0
        while R<len(s):
            if s[R] not in sett:
                maxL=max(maxL,R-L+1)
                sett.add(s[R])
                R+=1
            else:
                sett.remove(s[L])
                L+=1

        return maxL
