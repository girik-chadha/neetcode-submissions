class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #incase of 2 elements:
        if len(nums)==2:
            return [nums[1],nums[0]]

        if nums.count(0)>1:
            return [0]*len(nums)


        output_list=[1]*len(nums)
        prefix=1
        postfix=1
        for i in range(len(nums)):
            output_list[i] = prefix
            prefix=prefix*nums[i]
        for i in range(len(nums)-1, -1, -1):
            output_list[i]*=postfix
            postfix=postfix*nums[i]

        return output_list




        ''' THE O(N) idea is to use prefix and postfixes
        output_list=[1]*len(nums)
        L=[]
        R=[]
        temp_list=[]

        for i in range(0,len(nums)):
            final=1
            if i==0:
                for j in range(1,len(nums)):
                    output_list[i]=output_list[i]*nums[j]
            else:
                L=nums[:i]
                R=nums[i+1:]
                temp_list.extend(L)
                temp_list.extend(R)
                for j in temp_list:
                    final=final*j
                output_list[i]=final
            temp_list=[]
        return output_list
        '''
        