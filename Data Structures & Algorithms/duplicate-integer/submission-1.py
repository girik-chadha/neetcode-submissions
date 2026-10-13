class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        sett=set(nums)
        nums_dict=dict()
        count=0

        for i in sett:
            nums_dict[i]=0
        
        for i in nums:
            nums_dict[i]+=1
        
        for i in nums_dict:
            if nums_dict[i]>1:
                count+=1
        
        if count>=1:
            return True
        else:
            return False

        