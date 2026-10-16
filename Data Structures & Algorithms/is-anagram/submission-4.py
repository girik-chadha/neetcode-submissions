class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_t = {}
        count_s = {}

        for i in s:
            count_s[i] = count_s.get(i, 0) + 1
        for i in t:
            count_t[i] = count_t.get(i, 0) + 1
        
        if count_s == count_t:
            return True
        else:
            return False