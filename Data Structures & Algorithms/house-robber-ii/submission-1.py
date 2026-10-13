class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0],nums[1])
            
        rob1, rob2 = 0,0
        
        nums1=nums[1:len(nums)]
        nums2=nums[0:len(nums)-1]

        for n in nums1:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        max1=rob2

        rob1,rob2 = 0,0

        for n in nums2:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        max2=rob2

        return max(max1,max2)