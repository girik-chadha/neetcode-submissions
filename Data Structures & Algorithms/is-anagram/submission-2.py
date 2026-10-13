class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sett1=set(s)
        sett2=set(t)
        
        dict1=dict()
        dict2=dict()
        output_counter=0

        if sett1!=sett2:
            return False
        
        for i in sett1:
            dict1[i]=0
        for i in sett2:
            dict2[i]=0
        
        for i in s:
            dict1[i]+=1
        for i in t:
            dict2[i]+=1
        
        for i in dict1:
            if dict1[i]!=dict2[i]:
                return False
        return True
        
