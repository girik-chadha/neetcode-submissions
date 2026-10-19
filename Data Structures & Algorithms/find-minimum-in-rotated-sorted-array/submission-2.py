class Solution:
    def findMin(self, nums: List[int]) -> int:
        min1 = nums[0]

        L,R = 0, len(nums) - 1
        while L<=R:
            if nums[L]<nums[R]:
                min1 = min(min1, nums[L])
                break
            m = (L+R)//2
            min1 = min(min1, nums[m])
            if nums[m] >= nums[L]:
                L=m+1
            else:
                R=m-1
        return min1

        