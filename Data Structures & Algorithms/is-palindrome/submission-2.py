import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        sett=set(string.ascii_lowercase)
        list1=list(s)
        list2=[]

        #removing any non alphanumerics from the list
        for i in list1:
            if i.isalnum() == True:
                list2.append(i)
        

        
        return list2==list2[::-1]

        