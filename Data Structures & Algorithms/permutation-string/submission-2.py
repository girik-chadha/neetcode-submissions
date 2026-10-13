class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L, R = 0, 0
        count1 = {}
        count2 = {}
        output = False
        if len(s1)>len(s2):
            return False
            
        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
        
        while R<len(s2):
            while sum(count2.values()) < sum(count1.values()):
                count2[s2[R]] = count2.get(s2[R], 0) + 1
                R+=1
            if count2.items() <= count1.items():
                output = True
                R=len(s2)+1
            else:
                count2[s2[L]] -= 1
                if count2[s2[L]] == 0:
                    del count2[s2[L]]
                L+=1
                R=L+(len(s1)-1)
        return output


            