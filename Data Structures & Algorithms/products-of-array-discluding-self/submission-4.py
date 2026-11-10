class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==2:
            return [nums[1],nums[0]]

        l,r = 0, len(nums)-1
        L1 = []
        L2 = []
        output=[]
        while l<len(nums):
            if l-1==-1:
                L1.append(1)
                l+=1
            else:
                L1.append(nums[l-1]*L1[l-1])
                l+=1
        l=0
        while r>-1 and l<len(nums):
            if r+1==len(nums):
                L2.append(1)
                r-=1
                l+=1
            else:
                L2.append(nums[r+1]*L2[l-1])
                r-=1
                l+=1        
        L2.reverse()
        l1,l2=0,0
        while l1<len(L1) and l2<len(L2):
            output.append(L1[l1]*L2[l2])
            l1+=1
            l2+=1
        return output