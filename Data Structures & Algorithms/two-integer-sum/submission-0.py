class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        output_list=[0,0]
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    output_list[0]=i
                    output_list[1]=j
        return output_list
        