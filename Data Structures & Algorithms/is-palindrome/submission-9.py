class Solution:
    def isPalindrome(self, s: str) -> bool:
        lista=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
        s=s.lower()
        lists=[]
        for i in s:
            if i in lista:
                lists.append(i)
        L,R = 0, len(lists)-1
        out=True
        while L<R:
            if lists[L]!=lists[R]:
                out= False
            L+=1
            R-=1
        return out